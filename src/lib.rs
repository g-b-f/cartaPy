use pyo3::prelude::*;
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
        from_format,to_format, input_text, &reader_options, &writer_options
    );
    return  ret.expect("unexpected result");
}

#[pymodule]
fn _rust_wrapper(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(convert_text, m)?)?;
    Ok(())
}