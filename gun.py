import pygame, colors

from pygame.locals import *

MAX_H = 550
MIN_H = 50

class Gun:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.h = 10
        self.w = 30
        self.color = GUN_COLOR

    def draw(self, surf):     # draw gun on given surface
        self.r = (self.x, self.y, self.x+self.width, self.y+self.height)
        self.r.center = (self.x, self.y)
        pygame.draw.rect(surf, self.color, self.r)
        
    def fire(self, obj):
        bullet.v_x = 3

    def freeze(self, obj):
        self.y = y

    def move(self):
        self.x += self.
        
        
