import serial, pygame, math, sys, colors

from pygame.locals import *

# local variables

class Target:
    def __init__(self, SCREENHEIGHT):
        self.x = 575
        self.screenheight = SCREENHEIGHT
        self.y = random.random()*self.screenheight
        self.w = 20
        self.h = random.random()*100
        self.color = TARGET_COLOR
        self.rect = pygame.Rect((self.x, self.y, self.x+self.w, self.y+self.h))

    def draw(self, surf):
        self.rect.center = (self.x, self.y)
        pygame.draw.rect(surf, self.color, self.rect)

    def hitBy(self, obj):
        return self.rect.colliderect(obj.getRect())
        
    def moveTo(self, surf):
        if hitBy(obj):
            self.y = random.random()*self.screenheight
            self.h = random.random()*100


    
