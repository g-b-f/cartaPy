# generated programmatically. Do not edit.

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from carta import _rust_wrapper  # type: ignore[reportMissingModuleSource]
else:
    import _rust_wrapper


@dataclass
class From:
    _text: str
    from_fmt: str

    def _convert(self, to:str) -> str:
        return _rust_wrapper.convert_text(self.from_fmt, to, self._text)

    @property
    def to_commonmark(self):
        return self._convert("commonmark")

    @property
    def to_commonmark_x(self):
        return self._convert("commonmark_x")

    @property
    def to_markdown(self):
        return self._convert("markdown")

    @property
    def to_gfm(self):
        return self._convert("gfm")

    @property
    def to_markdown_strict(self):
        return self._convert("markdown_strict")

    @property
    def to_markdown_mmd(self):
        return self._convert("markdown_mmd")

    @property
    def to_markdown_phpextra(self):
        return self._convert("markdown_phpextra")

    @property
    def to_markdown_github(self):
        return self._convert("markdown_github")

    @property
    def to_json(self):
        return self._convert("json")

    @property
    def to_native(self):
        return self._convert("native")

    @property
    def to_html(self):
        return self._convert("html")

    @property
    def to_html5(self):
        return self._convert("html5")

    @property
    def to_html4(self):
        return self._convert("html4")

    @property
    def to_plain(self):
        return self._convert("plain")

    @property
    def to_csv(self):
        return self._convert("csv")

    @property
    def to_tsv(self):
        return self._convert("tsv")

    @property
    def to_opml(self):
        return self._convert("opml")

    @property
    def to_rst(self):
        return self._convert("rst")

    @property
    def to_ipynb(self):
        return self._convert("ipynb")

    @property
    def to_mediawiki(self):
        return self._convert("mediawiki")

    @property
    def to_dokuwiki(self):
        return self._convert("dokuwiki")

    @property
    def to_jira(self):
        return self._convert("jira")

    @property
    def to_man(self):
        return self._convert("man")

    @property
    def to_latex(self):
        return self._convert("latex")

    @property
    def to_org(self):
        return self._convert("org")

    @property
    def to_rtf(self):
        return self._convert("rtf")

    @property
    def to_docx(self):
        return self._convert("docx")

    @property
    def to_epub(self):
        return self._convert("epub")

    @property
    def to_epub3(self):
        return self._convert("epub3")

    @property
    def to_epub2(self):
        return self._convert("epub2")

    @property
    def to_odt(self):
        return self._convert("odt")

    @property
    def to_typst(self):
        return self._convert("typst")

    @property
    def to_asciidoc(self):
        return self._convert("asciidoc")

    @property
    def to_beamer(self):
        return self._convert("beamer")

    @property
    def to_revealjs(self):
        return self._convert("revealjs")

    @property
    def to_github_markdown(self):
        return self._convert("gfm")

    @property
    def to_jupyter(self):
        return self._convert("ipynb")

    @property
    def to_jupyter_notebook(self):
        return self._convert("ipynb")

    @property
    def to_restructuredtext(self):
        return self._convert("rst")

    @property
    def to_restructured_text(self):
        return self._convert("rst")

@dataclass
class Text:
    _text: str

    @property
    def from_commonmark(self):
        return From(self._text, "commonmark")

    @property
    def from_commonmark_x(self):
        return From(self._text, "commonmark_x")

    @property
    def from_markdown(self):
        return From(self._text, "markdown")

    @property
    def from_gfm(self):
        return From(self._text, "gfm")

    @property
    def from_markdown_strict(self):
        return From(self._text, "markdown_strict")

    @property
    def from_markdown_mmd(self):
        return From(self._text, "markdown_mmd")

    @property
    def from_markdown_phpextra(self):
        return From(self._text, "markdown_phpextra")

    @property
    def from_markdown_github(self):
        return From(self._text, "markdown_github")

    @property
    def from_json(self):
        return From(self._text, "json")

    @property
    def from_native(self):
        return From(self._text, "native")

    @property
    def from_html(self):
        return From(self._text, "html")

    @property
    def from_html5(self):
        return From(self._text, "html5")

    @property
    def from_html4(self):
        return From(self._text, "html4")

    @property
    def from_plain(self):
        return From(self._text, "plain")

    @property
    def from_csv(self):
        return From(self._text, "csv")

    @property
    def from_tsv(self):
        return From(self._text, "tsv")

    @property
    def from_opml(self):
        return From(self._text, "opml")

    @property
    def from_rst(self):
        return From(self._text, "rst")

    @property
    def from_ipynb(self):
        return From(self._text, "ipynb")

    @property
    def from_mediawiki(self):
        return From(self._text, "mediawiki")

    @property
    def from_dokuwiki(self):
        return From(self._text, "dokuwiki")

    @property
    def from_jira(self):
        return From(self._text, "jira")

    @property
    def from_man(self):
        return From(self._text, "man")

    @property
    def from_latex(self):
        return From(self._text, "latex")

    @property
    def from_org(self):
        return From(self._text, "org")

    @property
    def from_rtf(self):
        return From(self._text, "rtf")

    @property
    def from_docx(self):
        return From(self._text, "docx")

    @property
    def from_epub(self):
        return From(self._text, "epub")

    @property
    def from_epub3(self):
        return From(self._text, "epub3")

    @property
    def from_epub2(self):
        return From(self._text, "epub2")

    @property
    def from_odt(self):
        return From(self._text, "odt")

    @property
    def from_typst(self):
        return From(self._text, "typst")

    @property
    def from_asciidoc(self):
        return From(self._text, "asciidoc")

    @property
    def from_beamer(self):
        return From(self._text, "beamer")

    @property
    def from_revealjs(self):
        return From(self._text, "revealjs")

    @property
    def from_github_markdown(self):
        return From(self._text, "gfm")

    @property
    def from_jupyter(self):
        return From(self._text, "ipynb")

    @property
    def from_jupyter_notebook(self):
        return From(self._text, "ipynb")

    @property
    def from_restructuredtext(self):
        return From(self._text, "rst")

    @property
    def from_restructured_text(self):
        return From(self._text, "rst")

def convert(to_convert: str | Path):
    if isinstance(to_convert, Path):
        to_convert = to_convert.read_text()
    return Text(to_convert)
