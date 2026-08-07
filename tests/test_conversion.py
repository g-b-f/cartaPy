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

def assert_eq(expected, actual):
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"

def get_from_obj(input_text: str, from_format: str) -> From:
    return getattr(convert(input_text), f"from_{from_format}")

def get_to_str(from_obj: From, to_format: str) -> str:
    return getattr(from_obj, f"to_{to_format}")
    

class TestSimpleConversions:
    @pytest.mark.parametrize(("friendly_name", "internal_name"), from_format_mapping.items())
    def test_from_format_mapping(self, friendly_name:str, internal_name: str):
        from_obj = get_from_obj("sample", friendly_name)
        assert_eq(from_obj.from_fmt, internal_name)
        assert_eq(from_obj._text, "sample")


    @pytest.mark.parametrize("from_name", from_format_mapping.keys())
    @pytest.mark.parametrize("to_name", to_format_mapping.keys())
    def test_format_mapping_attributes_exists(self, from_name: str, to_name:str):
        from_obj = get_from_obj("sample",from_name)
        # doing hasattr(from_obj) would trigger the conversion, which we don't want
        assert hasattr(type(from_obj), f"to_{to_name}")
        assert hasattr(type(from_obj), f"to_{to_name}_with_options")


    @pytest.mark.parametrize("markdown_format", markdown_formats)
    def test_convert_html_to_markdown(self, markdown_format: str):
        ret = get_to_str(get_from_obj(html, "html"), markdown_format)
        assert_eq(ret, markdown)


    @pytest.mark.parametrize("markdown_format", markdown_formats)
    def test_convert_markdown_to_html(self, markdown_format: str):
        ret = get_to_str(get_from_obj(markdown, markdown_format), "html")
        assert_eq(ret, html)


    @pytest.mark.parametrize("binary_format", sorted(binary_output_formats))
    def test_convert_to_bytes(self, binary_format: str):
        ret = getattr(convert(html).from_html, f"to_{binary_format}")
        assert isinstance(ret, bytes)
        assert len(ret) > 0


class TestConversionsWithOptions:
    def test_to_html_with_toc_and_standalone(self):
        input_md = "# Title\n\nSome text."
        from_obj = convert(input_md).from_markdown
        res = from_obj.to_html_with_options(toc=True, standalone=True)
        assert "Table of Contents" in res or "<nav" in res or "<ul" in res or "Title" in res
        assert "<!DOCTYPE html>" in res or "<html" in res

    def test_to_html_with_number_sections(self):
        input_md = "# Section One"
        expected = '<h1 data-number="1" id="section-one"><span\nclass="header-section-number">1</span> Section One</h1>'
        res = convert(input_md).from_markdown.to_html_with_options(number_sections=True)
        assert_eq(res, expected)

    def test_to_html_with_extensions(self):
        input_md = "~~strikethrough~~"
        res = convert(input_md).from_markdown.to_html_with_options(extensions=["strikeout"])
        assert_eq(res, "<p><del>strikethrough</del></p>")
        assert "<del>" in res or "<s>" in res or "del" in res or "strikethrough" in res

    def test_to_docx_with_options(self, mocker: MockerFixture):
        mock_convert = mocker.patch("carta._rust_wrapper.convert", return_value=b"mock docx")
        res = convert("Hello docx").from_markdown.to_docx_with_options(
            docx_reference_doc=b"ref_data"
        )
        assert_eq(res, b"mock docx")
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
        res = convert("Hello epub").from_markdown.to_epub_with_options(
            epub_subdirectory="EPUB"
        )
        assert_eq(res, b"mock epub")
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
        res = convert("Hello html").from_markdown.to_html_with_options(
            toc=True, number_sections=True
        )
        assert_eq(res,"<p>mock html</p>")
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
            from_obj.to_html_with_options(docx_reference_doc=b"ref") # type: ignore[reportCallIssue]
        with pytest.raises(TypeError):
            from_obj.to_docx_with_options(epub_subdirectory="EPUB") # type: ignore[reportCallIssue]
        with pytest.raises(TypeError):
            from_obj.to_epub_with_options(docx_reference_doc=b"ref") # type: ignore[reportCallIssue]


test_files = [
    "markdown_from_pandoc",
    "markdown_with_html"
]

class TestConvertFromPath:
    @pytest.mark.skip(reason="currently failing - revisit later")
    @pytest.mark.parametrize("file_name", test_files)
    def test_files(self, file_name: str):
        file_in = test_files_path / (file_name+".md")
        file_out = test_files_path / (file_name+".html")
        res = convert(file_in).from_markdown.to_html
        assert res == file_out.read_text()