#Распять Иисуса

import pygame
from pygame import *
from pygame.locals import *

WIDTH = 1200
HEIGHT = 920
FPS = 60
SPEED = 30
BORDER = 15

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
        if self.rect.right > WIDTH:
            self.rect.left = 0
        if self.rect.left < 0:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT

    def mouse_motion(self):
        x, y = pygame.mouse.get_pos()
        if x >= self.rect.left and x <= self.rect.left+BORDER and y >= self.rect.top and y <= self.rect.bottom:
            self.rect.x += SPEED
        elif x <= self.rect.right and x > self.rect.right-BORDER and y >= self.rect.top and y <= self.rect.bottom:
           self.rect.x -= SPEED
        elif y <= self.rect.bottom and y > self.rect.bottom-BORDER and x >= self.rect.left and x <= self.rect.right:
            self.rect.y -= SPEED
        elif y >= self.rect.top and y < self.rect.top+BORDER and x >= self.rect.left and x <= self.rect.right:
            self.rect.y += SPEED

    def mouse_button(self):
        pos = pygame.mouse.get_pos()
        collide = self.rect.collidepoint(pos)
        if event.button == 1 and collide:
            self.image = pygame.Surface((WIDTH, HEIGHT))
            self.image = background_img2
            self.rect = self.image.get_rect()
            self.rect.center = (0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Распни Иисуса')
background_img = pygame.image.load('background12.png')
background_img2 = pygame.image.load('background2.jpg')
player_img = pygame.image.load('player_img4.png')
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
cursor_img = pygame.image.load('cursor.png')

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            player.mouse_motion()
        elif event.type == pygame.MOUSEBUTTONDOWN:
           player.mouse_button()

    screen.blit(background_img,(0,0))
    screen.blit(cursor_img, (pygame.mouse.get_pos()))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    pygame.display.update()

pygame.quit()