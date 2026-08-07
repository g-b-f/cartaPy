# generated programmatically. Do not edit.

from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, Sequence, Tuple

from .options import Extension, MathMethod, WrapMode
from . import _rust_wrapper  # type: ignore[reportMissingModuleSource]

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

    def to_asciidoc(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "asciidoc",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_beamer(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "beamer",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_commonmark(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "commonmark",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_commonmark_x(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "commonmark_x",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_docx(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
        docx_reference_doc: bytes | None = None,
    ) -> bytes:
        return self._convert_bytes(
            "docx",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
            docx_reference_doc=docx_reference_doc,
        )

    def to_dokuwiki(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "dokuwiki",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_epub(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
        epub_cover_image: bytes | None = None,
        epub_metadata_xml: str | None = None,
        epub_subdirectory: str | None = None,
        epub_split_level: int | None = None,
        epub_stylesheets: Sequence[str] | None = None,
    ) -> bytes:
        return self._convert_bytes(
            "epub",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
            epub_cover_image=epub_cover_image,
            epub_metadata_xml=epub_metadata_xml,
            epub_subdirectory=epub_subdirectory,
            epub_split_level=epub_split_level,
            epub_stylesheets=epub_stylesheets,
        )

    def to_epub2(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
        epub_cover_image: bytes | None = None,
        epub_metadata_xml: str | None = None,
        epub_subdirectory: str | None = None,
        epub_split_level: int | None = None,
        epub_stylesheets: Sequence[str] | None = None,
    ) -> bytes:
        return self._convert_bytes(
            "epub2",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
            epub_cover_image=epub_cover_image,
            epub_metadata_xml=epub_metadata_xml,
            epub_subdirectory=epub_subdirectory,
            epub_split_level=epub_split_level,
            epub_stylesheets=epub_stylesheets,
        )

    def to_epub3(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
        epub_cover_image: bytes | None = None,
        epub_metadata_xml: str | None = None,
        epub_subdirectory: str | None = None,
        epub_split_level: int | None = None,
        epub_stylesheets: Sequence[str] | None = None,
    ) -> bytes:
        return self._convert_bytes(
            "epub3",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
            epub_cover_image=epub_cover_image,
            epub_metadata_xml=epub_metadata_xml,
            epub_subdirectory=epub_subdirectory,
            epub_split_level=epub_split_level,
            epub_stylesheets=epub_stylesheets,
        )

    def to_gfm(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "gfm",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_html(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "html",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_html4(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "html4",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_ipynb(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "ipynb",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_jira(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "jira",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_json(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "json",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_latex(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "latex",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_man(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "man",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_markdown(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "markdown",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_markdown_github(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "markdown_github",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_markdown_mmd(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "markdown_mmd",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_markdown_phpextra(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "markdown_phpextra",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_markdown_strict(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "markdown_strict",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_mediawiki(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "mediawiki",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_native(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "native",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_odt(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> bytes:
        return self._convert_bytes(
            "odt",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_opml(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "opml",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_org(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "org",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_plain(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "plain",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_revealjs(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "revealjs",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_rst(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "rst",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_rtf(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "rtf",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

    def to_typst(self,
        *,
        wrap: WrapMode | None = None,
        columns: int | None = None,
        number_sections: bool = False,
        toc: bool = False,
        toc_depth: int | None = None,
        math_method: MathMethod | None = None,
        math_url: str | None = None,
        standalone: bool = False,
        template: str | None = None,
        template_dir: str | None = None,
        variables: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        metadata: Dict[str, str] | Sequence[Tuple[str, str]] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        extensions: Sequence[Extension] | Extension | str | None = None,
    ) -> str:
        return self._convert_text(
            "typst",
            wrap=wrap,
            columns=columns,
            number_sections=number_sections,
            toc=toc,
            toc_depth=toc_depth,
            math_method=math_method,
            math_url=math_url,
            standalone=standalone,
            template=template,
            template_dir=template_dir,
            variables=variables,
            metadata=metadata,
            highlight_style=highlight_style,
            no_highlight=no_highlight,
            idiomatic_highlight=idiomatic_highlight,
            greedy_paragraphs=greedy_paragraphs,
            extensions=extensions,
        )

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
