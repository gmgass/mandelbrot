import sys
import os

# Adiciona o caminho do .pyd/so
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../target/release')))

try:
    import rust_motor
    print("Sucesso\n")
except ImportError as e:
    print("Erro\n")
    sys.exit(1)

# Parâmetros de resolução para o teste
WIDTH, HEIGHT = 800, 600
MAX_ITER = 100

# Executa o cálculo no Rust
raw_bytes = rust_motor.calculate_mandelbrot(
    WIDTH, HEIGHT, -2.0, 1.0, -1.2, 1.2, MAX_ITER
)

print("\nRESULTADO:")
print(f"Vetor com {len(raw_bytes)} bytes do Rust.")
print(f"Tamanho esperado de bytes: {WIDTH * HEIGHT * 3}")