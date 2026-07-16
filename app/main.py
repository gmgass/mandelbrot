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