#!/usr/bin/env python3

import pygame
import sys
import time
import copy
import numpy as np
from random import randint



class tetramino:
    def __init__(self, startX, startY):
        self.numericImage = np.matrix()
        self.left = True
        self.Right = True
        self.rotatation = 0
        self.y= 0
        self.x = 5

    def erase(self, field):
        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i, j] ==1:
                    field[self.y + i, self.x + j] = 0

    def goDown(self, field):

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i , j] == 1:
                    if  i + 1 == len(self.numericImage):
                        if self.y + i + 1 >= len(field):
                            return True
                        if field[self.y + i + 1, self.x + j] == 1:
                            return True
                    
                    elif not self.numericImage[i + 1, j] == 1:
                        if self.y + i + 1 >= len(field):
                            return True
                        if field[self.y + i + 1, self.x + j] == 1:
                            return True

        self.erase(field)

        self.y +=1

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i, j] ==1:
                    field[self.y + i, self.x + j] = self.numericImage[i , j]

    def goRight(self, field):

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i , j] == 1:
                    if j + 1 == np.size(self.numericImage, 1):
                        if self.x + 1 + j >= np.size(field, 1):
                            return 
                        if field[self.y + i, self.x + j + 1] == 1:
                            return

                    elif not self.numericImage[i, j + 1] == 1:
                        if self.x + j + 1 >= np.size(field, 1):
                            return 
                        if field[self.y + i, self.x + j + 1] == 1:
                            return 

        self.erase(field)

        self.x +=1

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i, j] == 1:
                    print(self.y + i , self.x + j) 
                    field[self.y + i, self.x + j] = self.numericImage[i , j]

        self.left = True

    def goLeft(self, field):
 
        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i , j] == 1:

                    if j - 1 == 0:
                        if self.x - 1 < 0:
                            return 
                        if field[self.y + i, self.x - 1] == 1:
                            return

                    elif not self.numericImage[i, j - 1] == 1:
                        if self.x + j - 1 < 0:
                            return 
                        if field[self.y + i, self.x + j - 1] == 1:
                            return 

        self.erase(field)

        self.x -=1

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i, j] ==1:
                    field[self.y + i, self.x + j] = self.numericImage[i , j]
        
        self.Right = True

    
    def rotate(self, field):
        transposed = self.numericImage.transpose()
        if self.rotatation % 2 == 0:
            flipped = np.flip(transposed)
        else:
            flipped = transposed

        self.rotatation += 1
        
        for i in range(len(flipped)):
           for j in range(np.size(flipped, 1)):
               if flipped[i , j] == 1:
                   if field[self.y + i, self.x + j] == 1:
                        return

        self.erase(field)
        self.numericImage = flipped


        
        
        


class Hero(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.rotatation = 0

class OrangeRicky(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 0, 0, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.rotatation = 0

class BlueRicky(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.rotatation = 0

class Teewee(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.rotatation = 0

class Cleverland(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.rotatation = 0

class RhodeIsland(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.rotatation = 0

class SmashBoy(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.rotatation = 0


def draw(field, startx, starty, screen, color):
    for i in range(len(field)):
            for j in range(np.size(field, 1)): 
                if field[i , j] == 1:
                   p = pygame.Rect( startx + 25 * j, starty + 25 * i, 25, 25)
                   pygame.draw.rect(screen, color, p)


def main():
    
    size = width, height = 25*13, 720
    speed = [1, 1]
    black = 0, 0, 0
    blue = 42, 12, 240
    white = 255, 255, 255
    field = np.zeros( (28, 12) )

    clock = pygame.time.Clock() #10 x 40
    screen = pygame.display.set_mode(size)
    downBar = pygame.Rect(0,height - 25, 25 * 13, 25)
    sideleft = pygame.Rect(0, height - 25 * 25, 25, height - 120)
    sideRight = pygame.Rect(25 * 12, height - 25 * 25, 25, height - 120)
    hero = Hero(4, 0)
    orangeRicky = OrangeRicky(5, 1)
    blueRicky = BlueRicky(4, 1)
    teewee = Teewee(4, 1)
    cleverland = Cleverland(4, 1)
    rhodeIsland = RhodeIsland(4, 1)
    smashboy = SmashBoy(4, 1)
    tetramini = [hero, orangeRicky, blueRicky, teewee, cleverland, rhodeIsland, smashboy]
    nxt = True
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                print(*field, sep="\n")
                sys.exit()
        if nxt:
            tetramino = copy.copy(tetramini[randint(0,6)])
            nxt = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            tetramino.goRight(field)
        elif pressed[pygame.K_a]:
            tetramino.goLeft(field)
        elif pressed[pygame.K_SPACE]:
            tetramino.rotate(field)


        screen.fill(black)
        nxt = tetramino.goDown(field)
        print(field)
        print()
        draw(field, 0, 0, screen, white)
        pygame.draw.rect(screen, white, downBar)
        pygame.draw.rect(screen, white, sideleft)
        pygame.draw.rect(screen, white, sideRight)
        pygame.display.flip()
        time.sleep(0.25)




if __name__=="__main__":
    main()

