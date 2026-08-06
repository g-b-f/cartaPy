from pathlib import Path

tab = " "*4
tab2 = tab*2

init_file = Path(__file__).parent.parent / "carta" / "__init__.py"

formats = [
    "commonmark",
    "commonmark_x",
    "markdown",
    "gfm",
    "markdown_strict",
    "markdown_mmd",
    "markdown_phpextra",
    "markdown_github",
    "json",
    "native",
    "html",
    "html5",
    "html4",
    "plain",
    "csv",
    "tsv",
    "opml",
    "rst",
    "ipynb",
    "mediawiki",
    "dokuwiki",
    "jira",
    "man",
    "latex",
    "org",
    "rtf",
    "docx",
    "epub",
    "epub3",
    "epub2",
    "odt",
    "typst",
    "asciidoc",
    "beamer",
    "revealjs",
]
format_mapping_partial = {
    "github_markdown": "gfm",
    "jupyter": "ipynb",
    "jupyter_notebook": "ipynb",
    "restructured_text": "rst",
}

format_mapping = {fmt:fmt for fmt in formats} | format_mapping_partial



preamble ="""# generated programmatically. Do not edit.

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from carta import _rust_wrapper  # type: ignore[reportMissingModuleSource]
else:
    import _rust_wrapper

"""

convert_func ="""
def convert(to_convert: str | Path):
    if isinstance(to_convert, Path):
        to_convert = to_convert.read_text()
    return Text(to_convert)
"""

from_class = [
"""
@dataclass
class From:
    _text: str
    from_fmt: str

    def _convert(self, to:str) -> str:
        return _rust_wrapper.convert_text(self.from_fmt, to, self._text)
"""
]

text_class = [
"""
@dataclass
class Text:
    _text: str
"""
]

def main():

    for friendly_name, internal_name in format_mapping.items():
        from_class.append(f"{tab}@property")
        from_class.append(f"{tab}def to_{friendly_name}(self):")
        from_class.append(f'{tab2}return self._convert("{internal_name}")')
        from_class.append("")

        text_class.append(f"{tab}@property")
        text_class.append(f"{tab}def from_{friendly_name}(self):")
        text_class.append(f'{tab2}return From(self._text, "{internal_name}")')
        text_class.append("")
        


    with open(init_file, "w") as f:
        f.write(preamble)
        f.write("\n".join(from_class))
        f.write("\n".join(text_class))
        f.write(convert_func)

    print(f"Generated {init_file}")


if __name__ == "__main__":
    main()