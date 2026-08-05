from carta import convert

html = "<p><em>Hello</em> world!</p>"
markdown = "*Hello* world!"

def test_convert_html_to_markdown():
    ret = convert(html).from_html.to_markdown
    assert ret == markdown

def test_convert_markdown_to_html():
    ret = convert(markdown).from_markdown.to_html
    assert ret == html