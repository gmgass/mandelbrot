import sys
import os
import pygame

# Adiciona o caminho do .pyd/so
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../target/release')))

try:
    import rust_motor
    print("Sucesso\n")
except ImportError as e:
    print("\n[ERRO] módulo motor_rust não encontrado.")
    sys.exit(1)

# config. inicial da janela de interface
WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# limites iniciais de Mandelbrot (valores sugeridos pelo copilot)
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.2, 1.2
max_iter = 120

def render_mandelbrot():
    raw_rgb_bytes = rust_motor.calculate_mandelbrot(WIDTH, HEIGHT, xmin, xmax, ymin, ymax, max_iter)
    return pygame.image.frombuffer(bytes(raw_rgb_bytes), (WIDTH, HEIGHT), 'RGB')

fractal_image = render_mandelbrot()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fractal_image, (0, 0))
    pygame.display.flip()

pygame.quit()