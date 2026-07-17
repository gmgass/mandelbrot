use pyo3::prelude::*;
use rayon::prelude::*;

// Função matemática do fractal de Mandelbrot (calcula número de iterações antes de escapar para o infinito)
fn calculate_pixel(cx: f64, cy: f64, max_iter: u32) -> u32 {
    let mut zx = 0.0;
    let mut zy = 0.0;
    let mut i = 0;

    // Fórmula iterativa: Z_{n+1} = Z_n^2 + C. Se o módulo ultrapassar 2.0 (ou seja, Z^2 > 4.0), o ponto escapa
    while zx * zx + zy * zy <= 4.0 && i < max_iter {
        let temp = zx * zx - zy * zy + cx;
        zy = 2.0 * zx * zy + cy;
        zx = temp;
        i += 1;
    }
    i // Retorna o número de iterações antes de escapar
}


#[pyfunction]
fn calculate_mandelbrot(
    width: usize, height: usize, xmin: f64, xmax: f64, ymin: f64, ymax: f64, max_iter: u32
) -> PyResult<Vec<u8>> { // Vetor de byte que armazena o RGB
    let mut image = vec![0; width * height * 3];

    image.par_chunks_mut(width * 3).enumerate()
        .for_each(|(y, row)| {
            let cy = ymin + (y as f64 / height as f64) * (ymax - ymin);

            for x in 0..width {
                let cx = xmin + (x as f64 / width as f64) * (xmax - xmin);
                let iterations = calculate_pixel(cx, cy, max_iter);
                let tone = if iterations == max_iter {
                    0
                } else {
                    ((iterations as f64 / max_iter as f64) * 255.0) as u8
                };

                let idx = x * 3;
                row[idx] = tone;                         // Red
                row[idx + 1] = (tone as f32 * 0.5) as u8;    // Green
                row[idx + 2] = (tone as f32 * 0.8) as u8;    // Blue
            }
        });
    Ok(image) // Retorna o vetor de bytes completo para o Python
}


#[pymodule]
fn rust_motor(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_mandelbrot, m)?)?; // Registra a função matemática traduzida dentro do módulo Python
    Ok(())
}