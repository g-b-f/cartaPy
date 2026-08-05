from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from carta import _rust_wrapper # type: ignore[reportMissingModuleSource]
else:
    import _rust_wrapper

from pathlib import Path

@dataclass
class From:
    _text: str
    from_fmt: str

    def _convert(self, to:str) -> str:
        return _rust_wrapper.convert_text(self.from_fmt, to, self._text)

    @property
    def to_markdown(self):
        return self._convert("markdown")
    
    @property
    def to_html(self):
        return self._convert("html")


@dataclass
class Text:
    _text: str

    @property
    def from_markdown(self):
        return From(self._text, "markdown")

    @property
    def from_html(self):
        return From(self._text, "html")


def convert(input: str|Path):
    if isinstance(input, Path):
        input = input.read_text()
    return Text(input)