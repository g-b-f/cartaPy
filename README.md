<div align="center">

# CartaPy

**An easy and fast document converter, built on [carta](https://github.com/mfkrause/carta).**


<a href="https://pypi.org/project/cartapy">
<img alt="PyPI Version" src="https://img.shields.io/pypi/v/cartapy?cacheSeconds=3600">
<img alt="minimum python version" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpypi.org%2Fpypi%2Fcartapy%2Fjson&query=%24.info.requires_python&label=requires%20python&cacheSeconds=3600">
</a>
</div>
<br>

Using it is simple:

```python
from carta import convert

html = "<p><em>Hello</em> world!</p>"
markdown = convert(html).from_html.to_markdown()
markdown_with_options = convert(html).from_html.to_markdown(
    toc=True,
    wrap="None",
)

with open("example.docx", "rb") as f:
    html = convert(f).from_docx.to_html()

with open("example.docx", "wb") as f:
    docx = convert(html).from_html.to_docx()
    f.write(docx)
```