import sys
import os
import pygame

# Aponta para o diretório onde o compilador gera o arquivo .pyd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../target/release')))

try:
    import rust_motor
except ImportError as e:
    print("\n[ERRO] módulo 'rust_motor' não encontrado.")
    sys.exit(1)

# config. inicial da janela de interface
WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CLP: Fractal de Mandelbrot")

clock = pygame.time.Clock()

# limites iniciais de Mandelbrot (valores sugeridos pelo copilot)
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.2, 1.2
max_iter = 120

def render_mandelbrot():
    global xmin, xmax, ymin, ymax
    raw_rgb_bytes = rust_motor.calculate_mandelbrot(WIDTH, HEIGHT, xmin, xmax, ymin, ymax, max_iter)
    return pygame.image.frombuffer(bytes(raw_rgb_bytes), (WIDTH, HEIGHT), 'RGB')

# renderização inicial
fractal_image = render_mandelbrot()
needs_redraw = True

# variáveis para controle de movimento com mouse
dragging = False
prev_mouse_pos = (0, 0)

running = True
while running:
    clock.tick(60)  # Limita a 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Segura botão do mouse para arrastar
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão Esquerdo
                dragging = True
                prev_mouse_pos = pygame.mouse.get_pos()

        # Solta o botão do mouse e deixa de arrastar
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False

        # Captura o movimento de arrasto
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mx, my = pygame.mouse.get_pos()
                dx = mx - prev_mouse_pos[0]
                dy = my - prev_mouse_pos[1]
                
                # Se houve deslocamento do mouse
                if dx != 0 or dy != 0:
                    current_width = xmax - xmin
                    current_height = ymax - ymin
                    
                    # Converte o deslocamento de pixels para unidades do plano
                    offset_x = (dx / WIDTH) * current_width
                    offset_y = (dy / HEIGHT) * current_height
                    
                    # Move os limites na direção contrária ao arrasto
                    xmin -= offset_x
                    xmax -= offset_x
                    ymin -= offset_y
                    ymax -= offset_y
                    
                    prev_mouse_pos = (mx, my)
                    needs_redraw = True

        elif event.type == pygame.MOUSEWHEEL:
            mx, my = pygame.mouse.get_pos()

            # calcula a posição do cursor sobre o plano
            cx = xmin + (mx / WIDTH) * (xmax - xmin)
            cy = ymin + (my / HEIGHT) * (ymax - ymin)
            current_width = xmax - xmin
            current_height = ymax - ymin
            
            # Aplica o zoom
            if event.y > 0:
                zoom_factor = 0.85
            else:
                zoom_factor = 1.15
                
            new_width = current_width * zoom_factor
            new_height = current_height * zoom_factor
            
            proportion_x = mx / WIDTH
            proportion_y = my / HEIGHT
            
            # Recalcula os limites das bordas mantendo o cursor como ponto fixo
            xmin = cx - proportion_x * new_width
            xmax = xmin + new_width
            ymin = cy - proportion_y * new_height
            ymax = ymin + new_height
            
            needs_redraw = True

    # Solicita processamento apenas se houver interação do usuário
    if needs_redraw:
        fractal_image = render_mandelbrot()
        screen.blit(fractal_image, (0, 0))
        pygame.display.flip()
        needs_redraw = False

pygame.quit()