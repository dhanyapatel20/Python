import pygame
import random

pygame.init()

sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2

blue=pygame.Color("blue")
light_blue=pygame.Color("lightblue")
red=pygame.Color("red")

green=pygame.Color("green")
yellow=pygame.Color("yellow")
orange=pygame.Color("orange")
purple=pygame.Color("purple")

class ColorfulSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.randint(-1, 1), random.randint(-1, 1)]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))

    def change_color(self):
        self.image.fill(random.choice([green, yellow, orange, purple]))

def change_background_color():
    global background_color
    background_color = random.choice([blue, light_blue, red])

all_sprites = pygame.sprite.Group()
st1 = ColorfulSprite(purple, 50, 50)
st1.rect.x = random.randint(0, 450)
st1.rect.y = random.randint(0, 370)
all_sprites.add(st1)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colorful Sprite Game")
background_color = blue
screen.fill(background_color)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == sprite_color_change_event:
            st1.change_color()
        elif event.type == background_color_change_event:
            change_background_color()

    all_sprites.update()
    screen.fill(background_color)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)