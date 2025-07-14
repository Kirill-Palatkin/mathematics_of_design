import pygame
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain")

WHITE = (255, 255, 255)

background_image = pygame.image.load("images/sea.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

drop_image = pygame.image.load("images/raindrop.png").convert_alpha()
drop_image = pygame.transform.scale(drop_image, (10, 15))  # Масштабируем изображение капли


class Drop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-500, -50)
        self.speed = random.randint(10, 18)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-500, -50)
            self.x = random.randint(0, WIDTH)

    def show(self):
        screen.blit(drop_image, (self.x, self.y))


drops = [Drop() for _ in range(500)]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_image, (0, 0))

    for drop in drops:
        drop.fall()
        drop.show()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
