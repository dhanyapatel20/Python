import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

sky_blue = (135, 206, 235)

screen.fill((255, 255, 255))

pygame.draw.circle(screen, sky_blue, (300, 300), 100)
pygame.draw.circle(screen, sky_blue, (100, 100), 100, 3)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
