use std::sync::Arc;
use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyString};
use carta;


fn build_options(
    wrap: Option<&str>,
    columns: Option<usize>,
    number_sections: bool,
    toc: bool,
    toc_depth: Option<usize>,
    math_method: Option<&str>,
    math_url: Option<String>,
    standalone: bool,
    template: Option<String>,
    template_dir: Option<String>,
    variables: Option<Vec<(String, String)>>,
    metadata: Option<Vec<(String, String)>>,
    highlight_style: Option<String>,
    no_highlight: bool,
    idiomatic_highlight: bool,
    greedy_paragraphs: bool,
    extensions: Option<Vec<String>>,
    epub_cover_image: Option<Vec<u8>>,
    epub_metadata_xml: Option<String>,
    epub_subdirectory: Option<String>,
    epub_split_level: Option<usize>,
    epub_stylesheets: Option<Vec<String>>,
    docx_reference_doc: Option<Vec<u8>>,
) -> PyResult<(carta::ReaderOptions, carta::WriterOptions)> {
    let mut reader_options = carta::ReaderOptions::default();
    reader_options.greedy_paragraphs = greedy_paragraphs;

    let mut writer_options = carta::WriterOptions::default();

    if let Some(extension_list) = extensions {
        for extension in extension_list {
            let (is_remove, clean_name) = if extension.starts_with('-') {
                (true, &extension[1..])
            }
            else if extension.starts_with('+') {
                (false, &extension[1..])
            }
            else {
                (false, extension.as_str())
            };

            let Some(ext) = carta::Extension::from_name(clean_name) else { continue };
            if is_remove {
                reader_options.extensions.remove(ext);
                writer_options.extensions.remove(ext);
            } else {
                reader_options.extensions.insert(ext);
                writer_options.extensions.insert(ext);
            }
        }
    }

    if let Some(wrap_str) = wrap {
        writer_options.wrap = match wrap_str {
            "auto" => carta::WrapMode::Auto,
            "none" => carta::WrapMode::None,
            "preserve" => carta::WrapMode::Preserve,
            _ => return Err(PyRuntimeError::new_err(format!("Invalid wrap mode: {}", wrap_str))),
        };
    }

    writer_options.columns = columns;
    writer_options.number_sections = number_sections;
    writer_options.toc = toc;
    writer_options.toc_depth = toc_depth;

    if let Some(math_meth) = math_method {
        let url = math_url.unwrap_or_default();
        writer_options.math_method = match math_meth {
            "plain" => carta::MathMethod::Plain,
            "mathjax" => carta::MathMethod::MathJax(url),
            "katex" => carta::MathMethod::Katex(url),
            _ => return Err(PyRuntimeError::new_err(format!("Invalid math method: {}", math_meth))),
        };
    }

    if no_highlight {
        writer_options.highlight = carta::HighlightOptions::default();
    } else if idiomatic_highlight {
        writer_options.highlight = carta::HighlightOptions {
            idiomatic: true,
            ..carta::HighlightOptions::default()
        };
    } else if let Some(style) = highlight_style {
        if let Some(theme_res) = carta::builtin_style(&style) {
            let theme = theme_res.map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
            let highlighter = carta::Highlighter::new();
            writer_options.highlight = carta::HighlightOptions {
                highlighter: Some(Arc::new(highlighter)),
                theme: Some(theme),
                idiomatic: false,
            };
        } else if let Ok(bytes) = std::fs::read(&style) {
            let theme = carta::Theme::from_json(&bytes)
                .map_err(|e| PyRuntimeError::new_err(e.to_string()))?;
            let highlighter = carta::Highlighter::new();
            writer_options.highlight = carta::HighlightOptions {
                highlighter: Some(Arc::new(highlighter)),
                theme: Some(theme),
                idiomatic: false,
            };
        } else {
            return Err(PyRuntimeError::new_err(format!("Unknown highlight style: {}", style)));
        }
    }

    writer_options.standalone = standalone;
    if let Some(tmpl) = template {
        writer_options.standalone = true;
        writer_options.template = Some(Arc::from(tmpl));
    }
    if let Some(dir) = template_dir {
        writer_options.template_dir = Some(std::path::PathBuf::from(dir));
    }

    if let Some(vars) = variables {
        writer_options.variables = vars;
    }

    if let Some(meta) = metadata {
        for (k, v) in meta {
            writer_options.metadata.insert(k, carta::ast::MetaValue::MetaString(v.into()));
        }
    }

    // EPUB options
    let mut epub = carta::EpubOptions::default();
    if let Some(cover_bytes) = epub_cover_image {
        epub.cover_image = Some(("cover.jpg".to_string(), cover_bytes));
    }
    epub.metadata_xml = epub_metadata_xml;
    epub.subdirectory = epub_subdirectory;
    epub.split_level = epub_split_level;
    if let Some(sheets) = epub_stylesheets {
        epub.stylesheets = sheets;
    }
    writer_options.epub = Arc::new(epub);

    // DOCX options
    let mut docx = carta::DocxOptions::default();
    docx.reference_doc = docx_reference_doc;
    writer_options.docx = docx;

    Ok((reader_options, writer_options))
}

#[pyfunction]
#[pyo3(signature = (
    from_format,
    to_format,
    input_text,
    wrap = None,
    columns = None,
    number_sections = false,
    toc = false,
    toc_depth = None,
    math_method = None,
    math_url = None,
    standalone = false,
    template = None,
    template_dir = None,
    variables = None,
    metadata = None,
    highlight_style = None,
    no_highlight = false,
    idiomatic_highlight = false,
    greedy_paragraphs = false,
    extensions = None,
    epub_cover_image = None,
    epub_metadata_xml = None,
    epub_subdirectory = None,
    epub_split_level = None,
    epub_stylesheets = None,
    docx_reference_doc = None,
))]
fn convert_text(
    from_format: &str,
    to_format: &str,
    input_text: &str,
    wrap: Option<&str>,
    columns: Option<usize>,
    number_sections: bool,
    toc: bool,
    toc_depth: Option<usize>,
    math_method: Option<&str>,
    math_url: Option<String>,
    standalone: bool,
    template: Option<String>,
    template_dir: Option<String>,
    variables: Option<Vec<(String, String)>>,
    metadata: Option<Vec<(String, String)>>,
    highlight_style: Option<String>,
    no_highlight: bool,
    idiomatic_highlight: bool,
    greedy_paragraphs: bool,
    extensions: Option<Vec<String>>,
    epub_cover_image: Option<Vec<u8>>,
    epub_metadata_xml: Option<String>,
    epub_subdirectory: Option<String>,
    epub_split_level: Option<usize>,
    epub_stylesheets: Option<Vec<String>>,
    docx_reference_doc: Option<Vec<u8>>,
) -> PyResult<String> {
    let (reader_options, writer_options) = build_options(
        wrap,
        columns,
        number_sections,
        toc,
        toc_depth,
        math_method,
        math_url,
        standalone,
        template,
        template_dir,
        variables,
        metadata,
        highlight_style,
        no_highlight,
        idiomatic_highlight,
        greedy_paragraphs,
        extensions,
        epub_cover_image,
        epub_metadata_xml,
        epub_subdirectory,
        epub_split_level,
        epub_stylesheets,
        docx_reference_doc,
    )?;

    carta::convert_text(
        from_format,
        to_format,
        input_text,
        &reader_options,
        &writer_options,
    )
    .map_err(|err| PyRuntimeError::new_err(err.to_string()))
}

#[pyfunction]
#[pyo3(signature = (
    from_format,
    to_format,
    input_text,
    wrap = None,
    columns = None,
    number_sections = false,
    toc = false,
    toc_depth = None,
    math_method = None,
    math_url = None,
    standalone = false,
    template = None,
    template_dir = None,
    variables = None,
    metadata = None,
    highlight_style = None,
    no_highlight = false,
    idiomatic_highlight = false,
    greedy_paragraphs = false,
    extensions = None,
    epub_cover_image = None,
    epub_metadata_xml = None,
    epub_subdirectory = None,
    epub_split_level = None,
    epub_stylesheets = None,
    docx_reference_doc = None,
))]
fn convert(
    py: Python<'_>,
    from_format: &str,
    to_format: &str,
    input_text: &str,
    wrap: Option<&str>,
    columns: Option<usize>,
    number_sections: bool,
    toc: bool,
    toc_depth: Option<usize>,
    math_method: Option<&str>,
    math_url: Option<String>,
    standalone: bool,
    template: Option<String>,
    template_dir: Option<String>,
    variables: Option<Vec<(String, String)>>,
    metadata: Option<Vec<(String, String)>>,
    highlight_style: Option<String>,
    no_highlight: bool,
    idiomatic_highlight: bool,
    greedy_paragraphs: bool,
    extensions: Option<Vec<String>>,
    epub_cover_image: Option<Vec<u8>>,
    epub_metadata_xml: Option<String>,
    epub_subdirectory: Option<String>,
    epub_split_level: Option<usize>,
    epub_stylesheets: Option<Vec<String>>,
    docx_reference_doc: Option<Vec<u8>>,
) -> PyResult<Py<PyAny>> {
    let (reader_options, writer_options) = build_options(
        wrap,
        columns,
        number_sections,
        toc,
        toc_depth,
        math_method,
        math_url,
        standalone,
        template,
        template_dir,
        variables,
        metadata,
        highlight_style,
        no_highlight,
        idiomatic_highlight,
        greedy_paragraphs,
        extensions,
        epub_cover_image,
        epub_metadata_xml,
        epub_subdirectory,
        epub_split_level,
        epub_stylesheets,
        docx_reference_doc,
    )?;

    let output = carta::convert(
        from_format,
        to_format,
        input_text.as_bytes(),
        &reader_options,
        &writer_options,
    )
    .map_err(|err| PyRuntimeError::new_err(err.to_string()))?;

    match output {
        carta::Output::Text(text) => Ok(PyString::new(py, &text).into_any().unbind()),
        carta::Output::Bytes(bytes) => Ok(PyBytes::new(py, &bytes).into_any().unbind()),
    }
}

#[pymodule]
fn _rust_wrapper(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(convert_text, m)?)?;
    m.add_function(wrap_pyfunction!(convert, m)?)?;
    Ok(())
}
