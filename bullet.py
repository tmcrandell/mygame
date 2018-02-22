import pygame, colors, gun

from pygame.locals import *

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v_x = 0
        self.width = 10
        self.height = 5
        self.color = BULLET_COLOR
        self.rect = (0,0,self.width, self.height)

    def move(self):
        self.x + = self.v_x

    def fire(self, x, y):
        self.x = x
        self.y = y
    

    def draw(self, surf):
        self.rect.center = (self.x, self.y)
        pygame.draw.rect(surf, self.color, self.rect)

    def moveTo(self,y):
        self.x = 0
        self.y = y
