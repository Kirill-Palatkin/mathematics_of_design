import pygame
import math


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

wave_amplitude = 15  # Амплитуда волн
wave_frequency = 0.02  # Частота волн
wave_speed = 0.9
wave_offset_y = 115  # Смещение волны по высоте

background_image = pygame.image.load('images/miami2.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

ship_image = pygame.image.load('images/ship.png')
ship_image = pygame.transform.scale(ship_image, (100, 50))
ship_rect = ship_image.get_rect()

ship_x = 0
ship_y = HEIGHT // 2
ship_speed = 1.2  # Скорость движения корабля
ship_width = 100  # Ширина корабля

running = True
clock = pygame.time.Clock()
wave_offset = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    wave_points = []
    for x in range(WIDTH):
        y = HEIGHT - wave_offset_y - wave_amplitude * math.sin(wave_frequency * (x + wave_offset))
        wave_points.append((x, y))
    wave_offset += wave_speed

    pygame.draw.polygon(screen, "#04024F", wave_points + [(WIDTH, HEIGHT), (0, HEIGHT)], 0)

    ship_x += ship_speed
    if ship_x > WIDTH:
        ship_x = 0

    ship_wave_y = HEIGHT - wave_offset_y - wave_amplitude * math.sin(wave_frequency * (ship_x + wave_offset))

    next_x = ship_x + ship_speed
    next_wave_y = HEIGHT - wave_offset_y - wave_amplitude * math.sin(wave_frequency * (next_x + wave_offset))
    ship_angle = math.degrees(math.atan2(next_wave_y - ship_wave_y, ship_speed))

    rotated_ship = pygame.transform.rotate(ship_image, -ship_angle)
    rotated_rect = rotated_ship.get_rect(center=(ship_x, ship_wave_y))

    screen.blit(rotated_ship, rotated_rect.topleft)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
