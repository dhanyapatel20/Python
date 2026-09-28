import pygame

pygame.init()
screen=pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen, (254, 58, 50), (50, 50, 100, 100))
    pygame.display.update()