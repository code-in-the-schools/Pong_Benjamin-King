import pygame
import sys
import os

img_path = os.path.join('Ball1.png')


class Paddle(object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.draw.rect(screen, (0, 0, 0), (10, 10, 40, 100))
        self.rect = self.rect
        #self.rect = pygame.transform.scale(self.rect,(600,600))

        self.x = 200
        self.y = 300
        self.hitbox = (self.x, self.y, 205, 205)

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 0), (10, 10, 20, 90))

    def movement(self):
      if event.type == KEYDOWN
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.y -= 1
        if key[pygame.K_UP]:
            self.y += 1


class Ball(object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        Ball.image = pygame.image.load('Ball1.png')
        self.image = Ball.image
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.x = 50
        self.y = 50
        self.hitbox = (self.x, self.y, 55, 55)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

Sprite = Paddle()
Sprite1 = Ball()
running = True

while running:
    for event in pygame.event.get():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False




    screen.fill((255, 255, 255))
    Sprite.movement()
    Sprite.draw(screen)
    pygame.display.update()