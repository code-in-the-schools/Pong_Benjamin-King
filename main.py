import pygame
import sys
import os

img_path = os.path.join('Wall.png')
img_path = os.path.join('Blue.png')
img_path = os.path.join('Yellow.png')


class WallObj(object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        WallObj.image = pygame.image.load('Wall.png')

        self.image = pygame.transform.scale(self.image, (50, 50))

        self.x = 50
        self.y = 50
        self.x_velocity = 1
        self.y_velocity = 1

    def draw(self, surface):

        surface.blit(self.image, (self.x, self.y))

    def bounce(self, screen_width, screen_height, collider):
        self.x += self.x_velocity
        self.y += self.y_velocity

        if (self.y <= 0):
            self.y_velocity = 1

        if (self.y >= screen_height - 50):
            self.y_velocity = -1

        if (self.y >= screen_width - 50 or collider):
            self.x_velocity = -1

        if (self.x <= 0):
            self.x_velocity = 1


class Paddle(object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        Paddle.image = pygame.image.load('Blue.png')

        self.image = pygame.transform.scale(self.image, (20, 100))

        self.x = 10
        self.y = 100
        self.x_velocity = 1
        self.y_velocity = 1

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def move(self):
        pos = pygame.mouse.get_pos()

        self.y = pos[1]
        #self.x = pos[0]

    def hit(self, obj):
        if (obj.x + 25 >= self.x and obj.x + 25 <= self.x + 20):

            if (obj.y + 25 >= self.y and obj.y + 25 <= self.y + 100):

                print("True")
                return True
            else:
                return False


class walltop(object):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        walltop.image = pygame.image.load('Yellow.png')

        self.image = pygame.transform.scale(self.image, (700, 30))

        self.x = 0
        self.y = 700
        self.x_velocity = 1
        self.y_velocity = 1

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))



pygame.init()
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

Sprite1 = WallObj()
Sprite2 = Paddle()
bord = walltop()
running = True

while running:
    for event in pygame.event.get():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False

    screen.fill((255, 255, 255))
    Sprite1.draw(screen)
    Sprite2.draw(screen)
    bord.draw(screen)
    Sprite2.move()
    Sprite1.bounce(screen_height, screen_width, Sprite2.hit(Sprite1))
    pygame.display.update()
