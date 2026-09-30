# generated programmatically. Do not edit.

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from io import TextIOWrapper, BufferedReader

from . import _rust_wrapper  # type: ignore[reportMissingModuleSource]
from .options import Extension, MathMethod, WrapMode

def _get_binary_version() -> str:
    return _rust_wrapper.get_binary_version()


@dataclass
class From:
    _document: "Document"
    from_format: str

    @property
    def is_bytes(self) -> bool:
        return self._document.is_bytes

    def __repr__(self) -> str:
        return f"<From: convert {self._document!r} from {self.from_format}>"

    def _prepare_kwargs(self, kwargs: dict[str, Any]) -> dict[str, Any]:
        not_none = {k: v for k, v in kwargs.items() if v is not None}
        if "variables" in not_none and isinstance(not_none["variables"], dict):
            not_none["variables"] = list(not_none["variables"].items())
        if "metadata" in not_none and isinstance(not_none["metadata"], dict):
            not_none["metadata"] = list(not_none["metadata"].items())
        for key in ("enable_extensions", "disable_extensions"):
            if key in not_none:
                exts = not_none[key]
                if isinstance(exts, str):
                    not_none[key] = [exts]
                elif isinstance(exts, (set, tuple)):
                    not_none[key] = list(exts)
        return not_none

    @staticmethod
    def _with_disabled_extensions(format_name: str, disable_extensions: list[str]) -> str:
        # Disabled extensions are applied as `-ext` format-spec toggles, the only
        # removal path `carta` honors (the options union cannot subtract from a
        # format's default extension set).
        spec = format_name
        for ext in disable_extensions:
            spec += f"-{ext.lstrip('-')}"
        return spec

    def _convert_to_text(self, to: str, **kwargs: Any) -> str:
        kwargs = self._prepare_kwargs(kwargs)
        disable_extensions = kwargs.pop("disable_extensions", None) or []
        enable_extensions = kwargs.pop("enable_extensions", None)
        from_spec = self._with_disabled_extensions(self.from_format, disable_extensions)
        to_spec = self._with_disabled_extensions(to, disable_extensions)
        return _rust_wrapper.convert(from_spec, to_spec, self._document._data, extensions=enable_extensions, **kwargs) # type: ignore[return-value]

    def _convert_to_bytes(self, to: str, **kwargs: Any) -> bytes:
        kwargs = self._prepare_kwargs(kwargs)
        disable_extensions = kwargs.pop("disable_extensions", None) or []
        enable_extensions = kwargs.pop("enable_extensions", None)
        from_spec = self._with_disabled_extensions(self.from_format, disable_extensions)
        to_spec = self._with_disabled_extensions(to, disable_extensions)
        return _rust_wrapper.convert(from_spec, to_spec, self._document._data, extensions=enable_extensions, **kwargs) # type: ignore[return-value]

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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
        )

    def to_docbook(self,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
            "docbook",
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
        docx_reference_doc: bytes | None = None,
    ) -> bytes:
        return self._convert_to_bytes(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
        epub_cover_image: bytes | None = None,
        epub_metadata_xml: str | None = None,
        epub_subdirectory: str | None = None,
        epub_split_level: int | None = None,
        epub_stylesheets: list[str] | tuple[str] | set[str] | None = None,
    ) -> bytes:
        return self._convert_to_bytes(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
        epub_cover_image: bytes | None = None,
        epub_metadata_xml: str | None = None,
        epub_subdirectory: str | None = None,
        epub_split_level: int | None = None,
        epub_stylesheets: list[str] | tuple[str] | set[str] | None = None,
    ) -> bytes:
        return self._convert_to_bytes(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
        epub_cover_image: bytes | None = None,
        epub_metadata_xml: str | None = None,
        epub_subdirectory: str | None = None,
        epub_split_level: int | None = None,
        epub_stylesheets: list[str] | tuple[str] | set[str] | None = None,
    ) -> bytes:
        return self._convert_to_bytes(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> bytes:
        return self._convert_to_bytes(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
        )

    def to_github_markdown(self,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
        )

    def to_jupyter(self,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
        )

    def to_jupyter_notebook(self,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
        )

    def to_restructured_text(self,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
        )

    def to_multimarkdown(self,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> str:
        return self._convert_to_text(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
        )

    def to_open_document_text(self,
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
        variables: dict[str, str] | None = None,
        metadata: dict[str, str] | None = None,
        highlight_style: str | None = None,
        no_highlight: bool = False,
        idiomatic_highlight: bool = False,
        greedy_paragraphs: bool = False,
        enable_extensions: Iterable[Extension] | None = None,
        disable_extensions: Iterable[Extension] | None = None,
    ) -> bytes:
        return self._convert_to_bytes(
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
            enable_extensions=enable_extensions,
            disable_extensions=disable_extensions,
        )

@dataclass
class Document:
    _data: str | bytes

    @property
    def is_bytes(self) -> bool:
        return isinstance(self._data, bytes)

    def __repr__(self) -> str:
        if self.is_bytes:
            return f"<Document: {len(self._data)} bytes>"
        return f"<Document: {len(self._data)} characters>"
    

    @property
    def from_asciidoc(self):
        return From(self, "asciidoc")

    @property
    def from_beamer(self):
        return From(self, "beamer")

    @property
    def from_commonmark(self):
        return From(self, "commonmark")

    @property
    def from_commonmark_x(self):
        return From(self, "commonmark_x")

    @property
    def from_csv(self):
        return From(self, "csv")

    @property
    def from_docbook(self):
        return From(self, "docbook")

    @property
    def from_docx(self):
        return From(self, "docx")

    @property
    def from_dokuwiki(self):
        return From(self, "dokuwiki")

    @property
    def from_epub(self):
        return From(self, "epub")

    @property
    def from_gfm(self):
        return From(self, "gfm")

    @property
    def from_html(self):
        return From(self, "html")

    @property
    def from_html4(self):
        return From(self, "html4")

    @property
    def from_html5(self):
        return From(self, "html5")

    @property
    def from_ipynb(self):
        return From(self, "ipynb")

    @property
    def from_jira(self):
        return From(self, "jira")

    @property
    def from_json(self):
        return From(self, "json")

    @property
    def from_latex(self):
        return From(self, "latex")

    @property
    def from_man(self):
        return From(self, "man")

    @property
    def from_markdown(self):
        return From(self, "markdown")

    @property
    def from_markdown_mmd(self):
        return From(self, "markdown_mmd")

    @property
    def from_markdown_phpextra(self):
        return From(self, "markdown_phpextra")

    @property
    def from_markdown_strict(self):
        return From(self, "markdown_strict")

    @property
    def from_mediawiki(self):
        return From(self, "mediawiki")

    @property
    def from_native(self):
        return From(self, "native")

    @property
    def from_odt(self):
        return From(self, "odt")

    @property
    def from_opml(self):
        return From(self, "opml")

    @property
    def from_org(self):
        return From(self, "org")

    @property
    def from_plain(self):
        return From(self, "plain")

    @property
    def from_revealjs(self):
        return From(self, "revealjs")

    @property
    def from_rst(self):
        return From(self, "rst")

    @property
    def from_rtf(self):
        return From(self, "rtf")

    @property
    def from_tsv(self):
        return From(self, "tsv")

    @property
    def from_typst(self):
        return From(self, "typst")

    @property
    def from_github_markdown(self):
        return From(self, "gfm")

    @property
    def from_markdown_github(self):
        return From(self, "gfm")

    @property
    def from_jupyter(self):
        return From(self, "ipynb")

    @property
    def from_jupyter_notebook(self):
        return From(self, "ipynb")

    @property
    def from_restructured_text(self):
        return From(self, "rst")

    @property
    def from_multimarkdown(self):
        return From(self, "markdown_mmd")

    @property
    def from_open_document_text(self):
        return From(self, "odt")

def convert(to_convert: str | bytes | Path | TextIOWrapper | BufferedReader):
    if isinstance(to_convert, Path):
        to_convert = to_convert.read_text()
    elif isinstance(to_convert, (TextIOWrapper, BufferedReader)):
        to_convert = to_convert.read()
    return Document(to_convert)
