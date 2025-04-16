import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 11, 13
RADIUS = 33
PADDING = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Eyes")
clock = pygame.time.Clock()

eye_img = pygame.image.load("eye.png").convert_alpha()
eye_size = eye_img.get_width() // 2

circles = []
for i in range(ROWS):
    for j in range(COLS):
        x = PADDING + j * ((WIDTH - 2 * PADDING) // (COLS - 1))
        y = PADDING + i * ((HEIGHT - 2 * PADDING) // (ROWS - 1))
        circles.append((x, y))

running = True
while running:
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    for cx, cy in circles:
        pygame.draw.circle(screen, (255, 255, 255), (cx, cy), RADIUS)
        pygame.draw.circle(screen, (0, 0, 0), (cx, cy), RADIUS, 2)

        dx = mx - cx
        dy = my - cy
        angle = math.atan2(dy, dx)

        raw_distance = math.hypot(dx, dy)
        max_distance = RADIUS - eye_size - 5
        distance = min(raw_distance, max_distance)

        eye_x = cx + math.cos(angle) * distance
        eye_y = cy + math.sin(angle) * distance

        screen.blit(eye_img, (eye_x - eye_size, eye_y - eye_size))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
