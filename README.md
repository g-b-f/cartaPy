<div align="center">

# cartaPy

**An easy and fast document converter, built on [carta](https://github.com/mfkrause/carta)**


![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpypi.org%2Fpypi%2Fcartapy%2Fjson&query=%24.info.version&prefix=v&label=pypi&cacheSeconds=3600)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fpypi.org%2Fpypi%2Fcartapy%2Fjson&query=%24.info.requires_python&label=requires%20python&cacheSeconds=3600)

</div>

Using it is simple:

```python
from carta import convert

html = "<p><em>Hello</em> world!</p>"
markdown = convert(html).from_html.to_markdown
markdown_with_options = convert(html).from_html.to_markdown_with_options(
    toc=True,
    wrap="None",
)

with open("example.docx", "wb") as f:
    docx = convert(html).from_html.to_docx
    f.write(docx)
```