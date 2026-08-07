from pathlib import Path
from typing import Iterable

tab = " " * 4
tab2 = tab * 2
tab3 = tab * 3

init_file = Path(__file__).parent.parent / "carta" / "__init__.py"

formats = {
    "commonmark",
    "commonmark_x",
    "markdown",
    "gfm",
    "markdown_strict",
    "markdown_mmd",
    "markdown_phpextra",
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
}

format_mapping_extras = {
    "github_markdown": "gfm",
    "markdown_github": "gfm",
    "jupyter": "ipynb",
    "jupyter_notebook": "ipynb",
    "restructured_text": "rst",
    "multimarkdown": "markdown_mmd",
    "open_document_text": "odt"
}

epub_formats = {"epub", "epub2", "epub3"}
docx_formats = {"docx"}
binary_formats = epub_formats | docx_formats | {"odt"}

input_only_formats = {"html5", "csv", "tsv"}
output_only_formats: set[str] = set()

def get_format_mapping(includes: set[str], excludes: set[str]):
    format_set = (formats - excludes) | includes
    extras_subset = {k: v for k, v in format_mapping_extras.items() if v in format_set}
    return {fmt: fmt for fmt in sorted(format_set)} | extras_subset


from_format_mapping = get_format_mapping(input_only_formats, output_only_formats)
to_format_mapping = get_format_mapping(output_only_formats, input_only_formats)

preamble = """# generated programmatically. Do not edit.

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Sequence, Tuple

from . import _rust_wrapper  # type: ignore[reportMissingModuleSource]
from .options import Extension, MathMethod, WrapMode

"""

convert_func = """
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

    def _prepare_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        not_none = {k: v for k, v in kwargs.items() if v is not None}
        if "variables" in not_none and isinstance(not_none["variables"], dict):
            not_none["variables"] = list(not_none["variables"].items())
        if "metadata" in not_none and isinstance(not_none["metadata"], dict):
            not_none["metadata"] = list(not_none["metadata"].items())
        if "extensions" in not_none:
            exts = not_none["extensions"]
            if isinstance(exts, str):
                not_none["extensions"] = [exts]
            elif isinstance(exts, (set, tuple)):
                not_none["extensions"] = list(exts)
        return not_none

    def _convert_text(self, to: str, **kwargs: Any) -> str:
        return _rust_wrapper.convert_text(self.from_fmt, to, self._text, **self._prepare_kwargs(kwargs))

    def _convert_bytes(self, to: str, **kwargs: Any) -> bytes:
        return _rust_wrapper.convert(self.from_fmt, to, self._text, **self._prepare_kwargs(kwargs))  # type: ignore[return-value]
"""
]

text_class = [
    """
@dataclass
class Text:
    _text: str
"""
]

GLOBAL_OPTIONS = [
    ("wrap", "WrapMode | None", "None"),
    ("columns", "int | None", "None"),
    ("number_sections", "bool", "False"),
    ("toc", "bool", "False"),
    ("toc_depth", "int | None", "None"),
    ("math_method", "MathMethod | None", "None"),
    ("math_url", "str | None", "None"),
    ("standalone", "bool", "False"),
    ("template", "str | None", "None"),
    ("template_dir", "str | None", "None"),
    ("variables", "Dict[str, str] | Sequence[Tuple[str, str]] | None", "None"),
    ("metadata", "Dict[str, str] | Sequence[Tuple[str, str]] | None", "None"),
    ("highlight_style", "str | None", "None"),
    ("no_highlight", "bool", "False"),
    ("idiomatic_highlight", "bool", "False"),
    ("greedy_paragraphs", "bool", "False"),
    ("extensions", "Sequence[Extension] | Extension | str | None", "None"),
]

EPUB_OPTIONS = [
    ("epub_cover_image", "bytes | None", "None"),
    ("epub_metadata_xml", "str | None", "None"),
    ("epub_subdirectory", "str | None", "None"),
    ("epub_split_level", "int | None", "None"),
    ("epub_stylesheets", "Sequence[str] | None", "None"),
]

DOCX_OPTIONS = [
    ("docx_reference_doc", "bytes | None", "None"),
]


def render_params(params: Iterable[tuple[str, str, str]]) -> list[str]:
    return [f"{tab2}{name}: {type_annotation} = {default}," for name, type_annotation, default in params]

def render_call_args(params: Iterable[tuple[str, str, str]]) -> list[str]:
    return [f"{tab3}{name}={name}," for name, *_ in params]

def render_from_property(friendly_name: str, internal_name: str) -> list[str]:
    return [
        f"{tab}@property",
        f"{tab}def from_{friendly_name}(self):",
        f'{tab2}return From(self._text, "{internal_name}")',
        "",
    ]


def render_to_method(friendly_name: str, internal_name: str) -> list[str]:
    ret_type = "bytes" if internal_name in binary_formats else "str"
    conv_method = "_convert_bytes" if internal_name in binary_formats else "_convert_text"
    method_name = f"to_{friendly_name}"
    params = list(GLOBAL_OPTIONS)
    if internal_name in epub_formats:
        params += EPUB_OPTIONS
    if internal_name in docx_formats:
        params += DOCX_OPTIONS

    lines = [f"{tab}def {method_name}(self,", f"{tab2}*,"]
    lines.extend(render_params(params))
    lines.append(f"{tab}) -> {ret_type}:")
    lines.append(f"{tab2}return self.{conv_method}(")
    lines.append(f'{tab3}"{internal_name}",')
    lines.extend(render_call_args(params))
    lines.append(f"{tab2})")
    lines.append("")
    return lines


def main():
    for friendly_name, internal_name in to_format_mapping.items():
        from_class.extend(render_to_method(friendly_name, internal_name))

    for friendly_name, internal_name in from_format_mapping.items():
        text_class.extend(render_from_property(friendly_name, internal_name))

    with open(init_file, "w") as f:
        f.write(preamble)
        f.write("\n".join(from_class))
        f.write("\n".join(text_class))
        f.write(convert_func)

    print(f"Generated {init_file}")


if __name__ == "__main__":
    main()
