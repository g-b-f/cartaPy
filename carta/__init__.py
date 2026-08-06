# generated programmatically. Do not edit.

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import _rust_wrapper  # type: ignore[reportMissingModuleSource]
else:
    from . import _rust_wrapper


@dataclass
class From:
    _text: str
    from_fmt: str

    def _convert_text(self, to: str) -> str:
        return _rust_wrapper.convert_text(self.from_fmt, to, self._text)

    def _convert_bytes(self, to: str) -> bytes:
        return _rust_wrapper.convert(self.from_fmt, to, self._text)  # type: ignore[return-value]

    @property
    def to_asciidoc(self):
        return self._convert_text("asciidoc")

    @property
    def to_beamer(self):
        return self._convert_text("beamer")

    @property
    def to_commonmark(self):
        return self._convert_text("commonmark")

    @property
    def to_commonmark_x(self):
        return self._convert_text("commonmark_x")

    @property
    def to_docx(self):
        return self._convert_bytes("docx")

    @property
    def to_dokuwiki(self):
        return self._convert_text("dokuwiki")

    @property
    def to_epub(self):
        return self._convert_bytes("epub")

    @property
    def to_epub2(self):
        return self._convert_bytes("epub2")

    @property
    def to_epub3(self):
        return self._convert_bytes("epub3")

    @property
    def to_gfm(self):
        return self._convert_text("gfm")

    @property
    def to_html(self):
        return self._convert_text("html")

    @property
    def to_html4(self):
        return self._convert_text("html4")

    @property
    def to_ipynb(self):
        return self._convert_text("ipynb")

    @property
    def to_jira(self):
        return self._convert_text("jira")

    @property
    def to_json(self):
        return self._convert_text("json")

    @property
    def to_latex(self):
        return self._convert_text("latex")

    @property
    def to_man(self):
        return self._convert_text("man")

    @property
    def to_markdown(self):
        return self._convert_text("markdown")

    @property
    def to_markdown_github(self):
        return self._convert_text("markdown_github")

    @property
    def to_markdown_mmd(self):
        return self._convert_text("markdown_mmd")

    @property
    def to_markdown_phpextra(self):
        return self._convert_text("markdown_phpextra")

    @property
    def to_markdown_strict(self):
        return self._convert_text("markdown_strict")

    @property
    def to_mediawiki(self):
        return self._convert_text("mediawiki")

    @property
    def to_native(self):
        return self._convert_text("native")

    @property
    def to_odt(self):
        return self._convert_bytes("odt")

    @property
    def to_opml(self):
        return self._convert_text("opml")

    @property
    def to_org(self):
        return self._convert_text("org")

    @property
    def to_plain(self):
        return self._convert_text("plain")

    @property
    def to_revealjs(self):
        return self._convert_text("revealjs")

    @property
    def to_rst(self):
        return self._convert_text("rst")

    @property
    def to_rtf(self):
        return self._convert_text("rtf")

    @property
    def to_typst(self):
        return self._convert_text("typst")

@dataclass
class Text:
    _text: str

    @property
    def from_asciidoc(self):
        return From(self._text, "asciidoc")

    @property
    def from_beamer(self):
        return From(self._text, "beamer")

    @property
    def from_commonmark(self):
        return From(self._text, "commonmark")

    @property
    def from_commonmark_x(self):
        return From(self._text, "commonmark_x")

    @property
    def from_csv(self):
        return From(self._text, "csv")

    @property
    def from_docx(self):
        return From(self._text, "docx")

    @property
    def from_dokuwiki(self):
        return From(self._text, "dokuwiki")

    @property
    def from_epub(self):
        return From(self._text, "epub")

    @property
    def from_epub2(self):
        return From(self._text, "epub2")

    @property
    def from_epub3(self):
        return From(self._text, "epub3")

    @property
    def from_gfm(self):
        return From(self._text, "gfm")

    @property
    def from_html(self):
        return From(self._text, "html")

    @property
    def from_html4(self):
        return From(self._text, "html4")

    @property
    def from_html5(self):
        return From(self._text, "html5")

    @property
    def from_ipynb(self):
        return From(self._text, "ipynb")

    @property
    def from_jira(self):
        return From(self._text, "jira")

    @property
    def from_json(self):
        return From(self._text, "json")

    @property
    def from_latex(self):
        return From(self._text, "latex")

    @property
    def from_man(self):
        return From(self._text, "man")

    @property
    def from_markdown(self):
        return From(self._text, "markdown")

    @property
    def from_markdown_github(self):
        return From(self._text, "markdown_github")

    @property
    def from_markdown_mmd(self):
        return From(self._text, "markdown_mmd")

    @property
    def from_markdown_phpextra(self):
        return From(self._text, "markdown_phpextra")

    @property
    def from_markdown_strict(self):
        return From(self._text, "markdown_strict")

    @property
    def from_mediawiki(self):
        return From(self._text, "mediawiki")

    @property
    def from_native(self):
        return From(self._text, "native")

    @property
    def from_odt(self):
        return From(self._text, "odt")

    @property
    def from_opml(self):
        return From(self._text, "opml")

    @property
    def from_org(self):
        return From(self._text, "org")

    @property
    def from_plain(self):
        return From(self._text, "plain")

    @property
    def from_revealjs(self):
        return From(self._text, "revealjs")

    @property
    def from_rst(self):
        return From(self._text, "rst")

    @property
    def from_rtf(self):
        return From(self._text, "rtf")

    @property
    def from_tsv(self):
        return From(self._text, "tsv")

    @property
    def from_typst(self):
        return From(self._text, "typst")

def convert(to_convert: str | Path):
    if isinstance(to_convert, Path):
        to_convert = to_convert.read_text()
    return Text(to_convert)
