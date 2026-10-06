from pathlib import Path

import pytest
from pytest_mock import MockerFixture

from carta import From, convert
from utils.generate_init import (
    binary_formats,
    from_format_mapping,
    to_format_mapping,
)

html = "<p><em>Hello</em> world!</p>"
markdown = "*Hello* world!"

markdown_formats = [
    fmt for fmt, internal in to_format_mapping.items() if internal in ("markdown", "gfm")
]

def get_from_obj(input_text: str|bytes, from_format: str) -> From:
    return getattr(convert(input_text), f"from_{from_format}")

def get_conversion(from_obj: From, to_format: str) -> str |bytes:
    func = getattr(from_obj, f"to_{to_format}")
    return func()
    

class TestSimpleConversions:
    @pytest.mark.parametrize("markdown_format", markdown_formats)
    def test_convert_html_to_markdown(self, markdown_format: str):
        ret = get_conversion(get_from_obj(html, "html"), markdown_format)
        assert ret == markdown


    @pytest.mark.parametrize("markdown_format", markdown_formats)
    def test_convert_markdown_to_html(self, markdown_format: str):
        ret = get_conversion(get_from_obj(markdown, markdown_format), "html")
        assert ret == html


    @pytest.mark.parametrize("binary_format", sorted(binary_formats & set(to_format_mapping.values())))
    def test_convert_to_bytes(self, binary_format: str):
        ret = get_conversion(get_from_obj("sample", "markdown"), binary_format)
        assert isinstance(ret, bytes)
        assert len(ret) > 0

    @pytest.mark.parametrize("binary_format", sorted(binary_formats & set(from_format_mapping.values())))
    def test_convert_from_bytes(self, binary_format: str):
        binary = get_conversion(get_from_obj("sample", "markdown"), binary_format)
        get_conversion(get_from_obj(binary, binary_format), "markdown")


class TestConversionsWithOptions:
    def test_to_html_with_toc_and_standalone(self):
        input_md = "# Title\n\nSome text."
        from_obj = convert(input_md).from_markdown
        res = from_obj.to_html(toc=True, standalone=True)
        assert "<!DOCTYPE html>" in res
        assert '<nav id="TOC" role="doc-toc">' in res
        assert '<li><a href="#title" id="toc-title">Title</a></li>' in res
        assert '<h1 id="title">Title</h1>' in res
        assert '<p>Some text.</p>' in res

    def test_to_html_with_number_sections(self):
        input_md = "# Section One"
        expected = '<h1 data-number="1" id="section-one"><span\n'\
        'class="header-section-number">1</span> Section One</h1>'
        res = convert(input_md).from_markdown.to_html(number_sections=True)
        assert res == expected

    def test_enabled_extensions(self):
        input_md = "some\ntext"
        res = convert(input_md).from_markdown.to_html(enable_extensions=["hard_line_breaks"])
        assert res == "<p>some<br />\ntext</p>"

    def test_disabled_extensions(self):
        input_md = "<p><div>some text</div></p>"
        res = convert(input_md).from_html.to_gfm(disable_extensions=["raw_html"])
        assert res == "some text"

    def test_to_docx_with_options(self, mocker: MockerFixture):
        mock_convert = mocker.patch("carta._rust_wrapper.convert", return_value=b"mock docx")
        res = convert("Hello docx").from_markdown.to_docx(docx_reference_doc=b"ref_data")
        assert res == b"mock docx"
        mock_convert.assert_called_once_with(
            "markdown",
            "docx",
            "Hello docx",
            number_sections=False,
            toc=False,
            standalone=False,
            no_highlight=False,
            idiomatic_highlight=False,
            greedy_paragraphs=False,
            extensions=None,
            docx_reference_doc=b"ref_data",
        )

    def test_to_epub_with_options(self, mocker: MockerFixture):
        mock_convert = mocker.patch("carta._rust_wrapper.convert", return_value=b"mock epub")
        res = convert("Hello epub").from_markdown.to_epub(epub_subdirectory="EPUB")
        assert res == b"mock epub"
        mock_convert.assert_called_once_with(
            "markdown",
            "epub",
            "Hello epub",
            number_sections=False,
            toc=False,
            standalone=False,
            no_highlight=False,
            idiomatic_highlight=False,
            greedy_paragraphs=False,
            extensions=None,
            epub_subdirectory="EPUB",
        )

    def test_to_html_with_options(self, mocker: MockerFixture):
        mock_convert = mocker.patch("carta._rust_wrapper.convert", return_value="<p>mock html</p>")
        res = convert("Hello html").from_markdown.to_html(toc=True, number_sections=True)
        assert res == "<p>mock html</p>"
        mock_convert.assert_called_once_with(
            "markdown",
            "html",
            "Hello html",
            number_sections=True,
            toc=True,
            standalone=False,
            no_highlight=False,
            idiomatic_highlight=False,
            greedy_paragraphs=False,
            extensions=None,
        )

    def test_invalid_option_raises_type_error(self):
        from_obj = convert("Hello").from_markdown
        with pytest.raises(TypeError):
            from_obj.to_html(docx_reference_doc=b"ref") # type: ignore[reportCallIssue]
        with pytest.raises(TypeError):
            from_obj.to_docx(epub_subdirectory="EPUB") # type: ignore[reportCallIssue]
        with pytest.raises(TypeError):
            from_obj.to_epub(docx_reference_doc=b"ref") # type: ignore[reportCallIssue]


class TestConvertFromFile:
    test_files_path = Path(__file__).resolve().parent / "test_files"

    test_files = [
    "markdown_from_pandoc",
    "markdown_with_html"
    ]
    
    def test_basic_conversion(self, tmp_path:Path):
        file_in = tmp_path / "input.md"
        file_in.write_text(markdown)
        res = convert(file_in).from_markdown.to_html()
        assert res == html
        
    @pytest.mark.parametrize(
        ("file_name", "expected_fragments"),
        [
            (
                "markdown_from_pandoc",
                [
                    "<h1 id=\"introduction\">Introduction</h1>",
                    "Pandoc has long supported filters",
                    "Lua filter structure",
                    "return {",
                ],
            ),
            (
                "markdown_with_html",
                [
                    "<h1 id=\"markdown-syntax\">Markdown: Syntax</h1>",
                    "Inline HTML",
                    "Automatic Escaping for Special Characters",
                    "<a href=\"#overview\">Overview</a>",
                ],
            ),
        ],
    )
    def test_premade_files(self, file_name: str, expected_fragments: list[str]):
        file_in = self.test_files_path / (file_name + ".md")
        res = convert(file_in).from_markdown.to_html()

        assert res.strip().startswith("<h1")
        for fragment in expected_fragments:
            assert fragment in res

    def test_convert_from_opened_binary_file(self):
        with open(self.test_files_path/ "test.docx", "rb") as f:
            ret = convert(f).from_docx.to_markdown()
        assert ret == markdown

    def test_convert_from_opened_text_file(self):
        with open(self.test_files_path/ "test.html") as f:
            ret = convert(f).from_html.to_markdown()
        assert ret == markdown

    def test_convert_from_binary_Path(self):
        p = Path(self.test_files_path/ "test.docx").resolve()
        ret = convert(p).from_docx.to_markdown()
        assert ret == markdown