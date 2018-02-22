#!/usr/bin/python

import serial, pygame, sys
import colors, math, time

from pygame.locals import *

# code's global variables
HEIGHT = 600
WIDTH = 600
TARGET_HEIGHT = 60
FPS = 30
Ginst = "Game instructions: Start by placing your hand /r/n about 12 inches above the sensor. As you move/r/r your hand up and down, it will change the location/r/n of the gun, and when you are ready to fire, /r/n press the button. Good luck!"
TITLE = "Shooters"

s = serial.Serial("/dev/ttyACM0")

def draw_world(surf):
    # fill in background
    pygame.draw.rect(surf, BKGRND, (0,0,WIDTH,HEIGHT))

    # write and place title
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render(TITLE, True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = ((WIDTH/2),40)

    surf.blit(textSurfaceObj,textRectObj)


def main():
    pygame.init()
    pygame.display.init()
    fpsClock = pygame.time.Clock()

    SURF = pygame.display.set_mode((WIDTH, HEIGHT))  # creates game box
    pygame.display.set_caption(TITLE)     # window title

    # create game objects
    my_gun = gun.Gun(WIDTH/2,HEIGHT/2)
    my_target = target.Target(HEIGHT)
    my_bullet = bullet.Bullet(0,0)

    # print game instructions
    # include all instructions, with the request to hit
    # the button when finished and ready to start
    displayText(Ginst, SURF, "instruction")

    while (butt!=1):
        # empty loop that breaks when button is pressed
        # this allows user to read instructions at their own pace

    while True:
        # read in ultrasonic value
        l = s.readline()
        x = l.rstrip().split(",")
        H = x[0]
        butt = x[1]
        Hdiff = newH-H

        my_bullet.move(1.0/FPS)
        if (butt == 1):      # if the button is pressed
            my_gun.freeze()
            my_bullet.fire(my_gun.x,my_gun.y)
        if my_target.hitBy(my_bullet):
            displayText("Good shot!", SURF, "notice")
            my_target.moveTo(SURF)
        if (my_bullet.x > WIDTH):
            my_bullet.moveTo(my_gun.y)

            
        # updates game screen
        draw_world(SURF)
        my_gun.draw(SURF)
        my_target.draw(SURF)
        my_bullet.draw(SURF)
        pygame.display.update()
        fpsClock.tick(FPS)

        H = newH

        
def displayText(str, surf, type):

    if type == "instruction":
        center_location = (0, 100)
        F_SIZE = 20
        MSG_COLOR = BLACK
        MSG_BKGRND = WHITE

    if type == "notice":
        center_location = (WIDTH/2, HEIGHT/2)
        F_SIZE = 32
        MSG_COLOR = BLACK
        MSG_BKGRND = BKGRND


    fontObj = pygame.font.Font('freesansbold.ttf', F_SIZE)
    textSurfaceObj = fontObj.render(str, True, MSG_COLOR, MSG_BKGRND)      
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (center_location)


main()
