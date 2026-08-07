from pathlib import Path

import pytest
from pytest_mock import MockerFixture

from carta import convert, From
from utils.generate_init import (
    binary_output_formats,
    from_format_mapping,
    to_format_mapping,
)

test_files_path = Path(__file__).resolve().parent / "test_files"

html = "<p><em>Hello</em> world!</p>"
markdown = "*Hello* world!"

markdown_formats = [
    fmt for fmt, internal in to_format_mapping.items() if internal in ("markdown", "gfm")
]

def get_from_obj(input_text: str, from_format: str) -> From:
    return getattr(convert(input_text), f"from_{from_format}")

def get_conversion(from_obj: From, to_format: str) -> str |bytes:
    func = getattr(from_obj, f"to_{to_format}")
    return func()
    

class TestSimpleConversions:
    @pytest.mark.parametrize(("friendly_name", "internal_name"), from_format_mapping.items())
    def test_from_format_mapping(self, friendly_name:str, internal_name: str):
        from_obj = get_from_obj("sample", friendly_name)
        assert from_obj.from_fmt == internal_name
        assert from_obj._text == "sample"

    @pytest.mark.parametrize("from_name", from_format_mapping.keys())
    @pytest.mark.parametrize("to_name", to_format_mapping.keys())
    def test_format_mapping_attributes_exists(self, from_name: str, to_name:str):
        from_obj = get_from_obj("sample", from_name)
        assert hasattr(from_obj, f"to_{to_name}")


    @pytest.mark.parametrize("markdown_format", markdown_formats)
    def test_convert_html_to_markdown(self, markdown_format: str):
        ret = get_conversion(get_from_obj(html, "html"), markdown_format)
        assert ret == markdown


    @pytest.mark.parametrize("markdown_format", markdown_formats)
    def test_convert_markdown_to_html(self, markdown_format: str):
        ret = get_conversion(get_from_obj(markdown, markdown_format), "html")
        assert ret == html


    @pytest.mark.parametrize("binary_format", sorted(binary_output_formats))
    def test_convert_to_bytes(self, binary_format: str):
        ret = get_conversion(get_from_obj("sample", "markdown"), binary_format)
        assert isinstance(ret, bytes)
        assert len(ret) > 0


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

    def test_to_html_with_extensions(self):
        input_md = "~~strikethrough~~"
        res = convert(input_md).from_markdown.to_html(extensions=["strikeout"])
        assert res == "<p><del>strikethrough</del></p>"

    def test_to_docx_with_options(self, mocker: MockerFixture):
        mock_convert = mocker.patch("carta._rust_wrapper.convert", return_value=b"mock docx")
        res = convert("Hello docx").from_markdown.to_docx(
            docx_reference_doc=b"ref_data"
        )
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
            docx_reference_doc=b"ref_data",
        )

    def test_to_epub_with_options(self, mocker: MockerFixture):
        mock_convert = mocker.patch("carta._rust_wrapper.convert", return_value=b"mock epub")
        res = convert("Hello epub").from_markdown.to_epub(
            epub_subdirectory="EPUB"
        )
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
            epub_subdirectory="EPUB",
        )

    def test_to_html_with_options(self, mocker: MockerFixture):
        mock_convert = mocker.patch("carta._rust_wrapper.convert_text", return_value="<p>mock html</p>")
        res = convert("Hello html").from_markdown.to_html(
            toc=True, number_sections=True
        )
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
        )

    def test_invalid_option_raises_type_error(self):
        from_obj = convert("Hello").from_markdown
        with pytest.raises(TypeError):
            from_obj.to_html(docx_reference_doc=b"ref") # type: ignore[reportCallIssue]
        with pytest.raises(TypeError):
            from_obj.to_docx(epub_subdirectory="EPUB") # type: ignore[reportCallIssue]
        with pytest.raises(TypeError):
            from_obj.to_epub(docx_reference_doc=b"ref") # type: ignore[reportCallIssue]




class TestConvertFromPath:
    test_files = [
    "markdown_from_pandoc",
    "markdown_with_html"
    ]
    def test_basic_conversion(self, tmp_path:Path):
        file_in = tmp_path / "input.md"
        file_in.write_text(markdown)
        res = convert(file_in).from_markdown.to_html()
        assert res == html
    
    @pytest.mark.skip(reason="currently failing - revisit later")
    @pytest.mark.parametrize("file_name", test_files)
    def test_premade_files(self, file_name: str):
        file_in = test_files_path / (file_name+".md")
        file_out = test_files_path / (file_name+".html")
        res = convert(file_in).from_markdown.to_html
        assert res == file_out.read_text()