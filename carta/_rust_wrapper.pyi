from typing import Sequence

def get_binary_version() -> str:
    ...

def convert(
    from_format: str,
    to_format: str,
    input_text: str | bytes,
    wrap: str | None = None,
    columns: int | None = None,
    number_sections: bool = False,
    toc: bool = False,
    toc_depth: int | None = None,
    math_method: str | None = None,
    math_url: str | None = None,
    standalone: bool = False,
    template: str | None = None,
    template_dir: str | None = None,
    variables: Sequence[tuple[str, str]] | None = None,
    metadata: Sequence[tuple[str, str]] | None = None,
    highlight_style: str | None = None,
    no_highlight: bool = False,
    idiomatic_highlight: bool = False,
    greedy_paragraphs: bool = False,
    extensions: Sequence[str] | None = None,
    epub_cover_image: bytes | None = None,
    epub_metadata_xml: str | None = None,
    epub_subdirectory: str | None = None,
    epub_split_level: int | None = None,
    epub_stylesheets: Sequence[str] | None = None,
    docx_reference_doc: bytes | None = None,
) -> str | bytes: ...

