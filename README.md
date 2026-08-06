# cartaPy

An easy and fast document converter, built on [carta](https://github.com/mfkrause/carta)

Using it is simple:

```python
from carta import convert

html = "<p><em>Hello</em> world!</p>"
markdown = convert(html).from_html.to_markdown

with open("example.docx", "wb") as f:
    docx = convert(html).from_html.to_docx
    f.write(docx)
```