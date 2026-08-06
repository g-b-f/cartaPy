import pytest

from carta import convert
from utils.generate_init import (
    binary_output_formats,
    from_format_mapping,
    to_format_mapping,
)

html = "<p><em>Hello</em> world!</p>"
markdown = "*Hello* world!"

markdown_formats = [
    fmt for fmt, internal in to_format_mapping.items() if internal in ("markdown", "gfm")
]

class TestSimpleConversions:
    @pytest.mark.parametrize(("friendly_name", "internal_name"), from_format_mapping.items())
    def test_from_format_mapping(self, friendly_name, internal_name):
        from_obj = getattr(convert("sample"), f"from_{friendly_name}")
        assert from_obj.from_fmt == internal_name
        assert from_obj._text == "sample"


    @pytest.mark.parametrize("friendly_name", to_format_mapping.keys())
    def test_to_format_mapping_attribute_exists(self, friendly_name):
        from_obj = convert("sample").from_html
        assert hasattr(from_obj, f"to_{friendly_name}")
        assert hasattr(from_obj, f"to_{friendly_name}_with_options")


    @pytest.mark.parametrize("markdown_format", markdown_formats)
    def test_convert_html_to_markdown(self, markdown_format):
        ret = getattr(convert(html).from_html, f"to_{markdown_format}")
        assert ret == markdown


    @pytest.mark.parametrize("markdown_format", markdown_formats)
    def test_convert_markdown_to_html(self, markdown_format):
        ret = getattr(convert(markdown), f"from_{markdown_format}").to_html
        assert ret == html


    @pytest.mark.parametrize("binary_format", sorted(binary_output_formats))
    def test_convert_to_bytes(self, binary_format):
        ret = getattr(convert(html).from_html, f"to_{binary_format}")
        assert isinstance(ret, bytes)
        assert len(ret) > 0


class TestWithOptionsConversions:
    def test_to_html_with_toc_and_standalone(self):
        input_md = "# Title\n\nSome text."
        from_obj = convert(input_md).from_markdown
        res = from_obj.to_html_with_options(toc=True, standalone=True)
        assert "Table of Contents" in res or "<nav" in res or "<ul" in res or "Title" in res
        assert "<!DOCTYPE html>" in res or "<html" in res

    def test_to_html_with_number_sections(self):
        input_md = "# Section One"
        res = convert(input_md).from_markdown.to_html_with_options(number_sections=True)
        assert "1" in res

    def test_to_html_with_extensions(self):
        input_md = "~~strikethrough~~"
        res = convert(input_md).from_markdown.to_html_with_options(extensions=["strikeout"])
        assert "<del>" in res or "<s>" in res or "del" in res or "strikethrough" in res

    def test_to_docx_with_options(self, mocker):
        mock_convert = mocker.patch("carta._rust_wrapper.convert", return_value=b"mock docx")
        res = convert("Hello docx").from_markdown.to_docx_with_options(
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

    def test_to_epub_with_options(self, mocker):
        mock_convert = mocker.patch("carta._rust_wrapper.convert", return_value=b"mock epub")
        res = convert("Hello epub").from_markdown.to_epub_with_options(
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

    def test_to_html_with_options(self, mocker):
        mock_convert = mocker.patch("carta._rust_wrapper.convert_text", return_value="<p>mock html</p>")
        res = convert("Hello html").from_markdown.to_html_with_options(
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
            from_obj.to_html_with_options(docx_reference_doc=b"ref") # type: ignore[reportCallIssue]
        with pytest.raises(TypeError):
            from_obj.to_docx_with_options(epub_subdirectory="EPUB") # type: ignore[reportCallIssue]
        with pytest.raises(TypeError):
            from_obj.to_epub_with_options(docx_reference_doc=b"ref") # type: ignore[reportCallIssue]

