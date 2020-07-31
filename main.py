import pygame
import sys
import os
img_path = os.path.join('Ball.png')
img_path = os.path.join('Rect.png')

class Ball(object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(self.image,(600,600))

        Paddle.image = pygame.image.load('Ball.png')
        self.image = Paddle.image

        self.x = 200
        self.y = 200
        self.hitbox = (self.x, self.y, 205, 205)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))



class Paddle(object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        Paddle.image = pygame.image.load('Rect.png')
        self.image = Paddle.image
        

        self.x = 200
        self.y = 200
        self.hitbox = (self.x, self.y, 205, 205)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

Sprite = Ball()
Sprite = Paddle()

running = True
while running:
    for event in pygame.event.get():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False

    screen.fill((255, 255, 255))
    Sprite.draw(screen)

pygame.display.update()

