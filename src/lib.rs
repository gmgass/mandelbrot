use pyo3::prelude::*;

#[pyfunction]
fn integration_test(xmin: f64, xmax: f64, max_iter: u32) -> PyResult<String> {
    let _plane_width = xmax - xmin;
    let _xmin = xmin;
    let _xmax = xmax;
    let _max_iter = max_iter;
    
    let response = "Ponte funcionando.\n".to_string();
    Ok(response)
}

#[pymodule]
fn rust_motor(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(integration_test, m)?)?; // Registra a função traduzida dentro do módulo Python
    Ok(())
}