    use pyo3::prelude::*;

    #[pymodule]
    fn rust_motor(m: &Bound<'_, PyModule>) -> PyResult<()> {
        Ok(())
    }