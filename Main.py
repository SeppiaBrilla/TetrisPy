#!/usr/bin/env python3

import pygame
import sys
import time
import numpy as np
from random import randint



class tetramino:
    def __init__(self, startX, startY):
        self.numericImage = np.matrix()
        self.y= 0
        self.x = 5

    def goDown(self, field):  

        DownMostx = 0 
        DownMosty = 0
        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i , j] == 1 and i > DownMosty:
                    DownMosty = i
                    DownMostx = j

        if DownMosty + self.y + 1> len(field) - 1:
            return True

        if field[self.y + DownMosty + 1, self.x + DownMostx] == 1:
            return True

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                try:
                    if self.numericImage[i, j] == 1:
                        field[self.y + i, self.x + j] = 0
                except:
                    pass

        self.y +=1

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                try:
                    field[self.y + i, self.x + j] = self.numericImage[i , j]
                except:
                    if self.numericImage[i , j] == 1:
                        print("ERRORE")
                        sys.exit()

    def goRight(self, field):
        
        RightMostx = 0 
        RightMosty = 0
        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i , j] == 1 and j > RightMostx:
                    RightMosty = i
                    RightMostx = j

        if RightMostx + self.x + 1 > np.size(field, 1) - 1:
            return 

        if field[self.y + RightMosty, self.x + RightMostx + 1] == 1:
            return

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                try:
                    if self.numericImage[i, j] == 1:
                        field[self.y + i, self.x + j] = 0
                except:
                    pass

        self.x +=1

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                try:
                    field[self.y + i, self.x + j] = self.numericImage[i , j]
                except:
                    if self.numericImage[i , j] == 1:
                        print("ERRORE")
                        sys.exit()


    def goLeft(self, field):
 
        LeftMostx = 0 
        LeftMosty = 0
        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i , j] == 1 and j < LeftMostx:
                    LeftMosty = i
                    LeftMostx = j

        if LeftMostx + self.x - 1 < 0:
            return 

        if field[self.y + LeftMosty, self.x + LeftMostx - 1] == 1:
            return 

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                try:
                    if self.numericImage[i, j] == 1:
                        field[self.y + i, self.x + j] = 0
                except:
                    pass

        self.x -=1

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                try:
                    field[self.y + i, self.x + j] = self.numericImage[i , j]
                except:
                    if self.numericImage[i , j] == 1:
                        print("ERRORE")
                        sys.exit()

    
    def rotate(self, field):
        pass


        
        
        


class Hero(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

class OrangeRicky(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 0, 0, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])

class BlueRicky(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

class Teewee(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])

class Cleverland(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])

class RhodeIsland(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

class SmashBoy(tetramino):

    def __init__(self, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])


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
            tetramino = tetramini[randint(0,6)]
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

