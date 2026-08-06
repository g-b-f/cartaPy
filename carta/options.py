from typing import Literal

WrapMode = Literal["auto", "none", "preserve"]
MathMethod = Literal["plain", "mathjax", "katex"]

Extension = Literal[
    "smart",
    "strikeout",
    "superscript",
    "subscript",
    "pipe_tables",
    "footnotes",
    "task_lists",
    "autolink_bare_uris",
    "tex_math_dollars",
    "fenced_divs",
    "bracketed_spans",
    "hard_line_breaks",
    "raw_html",
    "header_attributes",
    "fenced_code_attributes",
    "inline_code_attributes",
    "link_attributes",
    "attributes",
    "definition_lists",
    "grid_tables",
    "multiline_tables",
    "simple_tables",
    "table_captions",
    "line_blocks",
    "fancy_lists",
    "example_lists",
    "startnum",
    "yaml_metadata_block",
    "pandoc_title_block",
    "auto_identifiers",
    "gfm_auto_identifiers",
]
