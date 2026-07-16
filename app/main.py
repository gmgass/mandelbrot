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

print("teste de ponte do Python para o Rust...\n")
return_message = rust_motor.integration_test(-2.0, 1.0, 150)

print("\nRESPOSTA DO RUST:")
print(return_message)