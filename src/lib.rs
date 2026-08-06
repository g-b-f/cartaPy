use pyo3::exceptions::PyRuntimeError;
use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyString};
use carta;


#[pyfunction]
fn convert_text(
    from_format: &str,
    to_format: &str,
    input_text: &str
) -> String {
    let reader_options = carta::ReaderOptions::default();
    let writer_options = carta::WriterOptions::default();

    let ret = carta::convert_text(
        from_format, to_format, input_text, &reader_options, &writer_options
    );
    ret.expect("unexpected result")
}

#[pyfunction]
fn convert(
    from_format: &str,
    to_format: &str,
    input_text: &str
) -> PyResult<PyObject> {
    let reader_options = carta::ReaderOptions::default();
    let writer_options = carta::WriterOptions::default();

    let output = carta::convert(
        from_format,
        to_format,
        input_text.as_bytes(),
        &reader_options,
        &writer_options,
    )
    .map_err(|err| PyRuntimeError::new_err(err.to_string()))?;

    Python::with_gil(|py| match output {
        carta::Output::Text(text) => Ok(PyString::new(py, &text).into()),
        carta::Output::Bytes(bytes) => Ok(PyBytes::new(py, &bytes).into()),
    })
}

#[pymodule]
fn _rust_wrapper(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(convert_text, m)?)?;
    m.add_function(wrap_pyfunction!(convert, m)?)?;
    Ok(())
}