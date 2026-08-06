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


@pytest.mark.parametrize(("friendly_name", "internal_name"), from_format_mapping.items())
def test_from_format_mapping(friendly_name, internal_name):
    from_obj = getattr(convert("sample"), f"from_{friendly_name}")
    assert from_obj.from_fmt == internal_name
    assert from_obj._text == "sample"


@pytest.mark.parametrize("friendly_name", to_format_mapping.keys())
def test_to_format_mapping_attribute_exists(friendly_name):
    from_obj = convert("sample").from_html
    assert hasattr(from_obj, f"to_{friendly_name}")


@pytest.mark.parametrize("markdown_format", markdown_formats)
def test_convert_html_to_markdown(markdown_format):
    ret = getattr(convert(html).from_html, f"to_{markdown_format}")
    assert ret == markdown


@pytest.mark.parametrize("markdown_format", markdown_formats)
def test_convert_markdown_to_html(markdown_format):
    ret = getattr(convert(markdown), f"from_{markdown_format}").to_html
    assert ret == html


@pytest.mark.parametrize("binary_format", sorted(binary_output_formats))
def test_convert_to_bytes(binary_format):
    ret = getattr(convert(html).from_html, f"to_{binary_format}")
    assert isinstance(ret, bytes)
    assert len(ret) > 0
