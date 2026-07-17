# Fractal de Mandelbrot: Rust e Python
**Autor: Gustavo Gass**

Projeto desenvolvido como exercício de integração entre linguagens distintas para a disciplina de Conceitos de Linguagem de Programação. Consiste na utilização de **Rust** para cálculo do **Conjunto de Mandelbrot** e **Python (pygame)** para interface gráfica.


## Estrutura do Repositório
*   `src/lib.rs`: Código fonte em Rust, responsável pelo cálculo matemático do fractal.
*   `Cargo.toml`: Gerenciador de dependências e configuração da biblioteca de ligação dinâmica (cdylib).
*   `app/main.py`: Código em python, responsável pela interface gráfica que utiliza a biblioteca compilada.
*   `Makefile`: Automação de compilação e execução do programa.

## Requisitos para execução
Para compilar e executar o projeto, é necessário:
*   Um compilador C (MinGW/GCC).
*   [Rust (Cargo)](https://www.rust-lang.org/tools/install)
*   [Python 3.x](https://www.python.org/downloads/)
*   [Pygame](https://www.pygame.org/)


## Como compilar e executar
A automação do projeto foi estruturada utilizando o `Makefile` na raiz do repositório.

Para compilar o código e executar em linux, macOS ou Windows via WSL, utilize:
*   make build
*   make run


Para compilar e executar em windows via MinGw, utilize:
*   mingw32-make build
*   mingw-make run
