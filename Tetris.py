#!/usr/bin/env python3

import pygame
import sys
import time
import copy
import numpy as np
from random import randint

#          balck       white               cyan           blue          orange         yellow          green          purple        red 

color = [(0, 0, 0), (255, 255, 255), (52, 235, 198), (42, 12, 240), (235, 159, 52), (250, 246, 0), (79, 250, 0), (145, 15, 189), (189, 15, 15) ]

class tetramino:
    def __init__(self, startX, startY):
        self.numericImage = np.matrix()
        self.left = True
        self.Right = True
        self.rotatation = 0
        self.y= 0
        self.x = 5

    def fit(self, field):
        for i in range(len(self.numericImage)):
               for j in range(np.size(self.numericImage, 1)):
                    if self.numericImage[i , j] and field[self.y + i, self.x + j]:
                        return False
    
        return True

    def draw(self, field):
        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i, j]:
                    field[self.y + i, self.x + j] = self.numericImage[i , j]

    def erase(self, field):
        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i, j]:
                    field[self.y + i, self.x + j] = 0

    def goDown(self, field):

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
               if self.numericImage[i , j] and self.y + i + 1 >= len(field):
                        return True
        

        self.erase(field)

        self.y +=1

        if self.fit(field):
            self.draw(field)
        else:
            self.y -=1
            self.draw(field)
            return True

    def goRight(self, field):

        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i , j] and self.x + 1 + j >= np.size(field, 1):
                    return

        self.erase(field)

        self.x +=1

        if self.fit(field):
            self.draw(field)
        else:
            self.x -=1
            self.draw(field)

    def goLeft(self, field):
 
        for i in range(len(self.numericImage)):
            for j in range(np.size(self.numericImage, 1)):
                if self.numericImage[i , j] and self.x - 1 + j < 0 :
                    return

        self.erase(field)

        self.x -=1

        if self.fit(field):
            self.draw(field)
        else:
            self.x +=1
            self.draw(field)

    
    def rotate(self, field):
        flipped = np.rot90(self.numericImage,1)


        for i in range(len(flipped)):
           for j in range(np.size(flipped, 1)):
               if flipped[i,j] and (0 > self.y + i or self.y + i >= len(field) or  0 > self.x + j or self.x + j >= np.size(field, 1)):
                        return 

        self.erase(field)

        original = self.numericImage

        self.numericImage = flipped

        if self.fit(field):
            self.draw(field)
        else:
            self.numericImage = original
            self.draw(field)


        
        
        


class Hero(tetramino):

    def __init__(self, numericX, numericY):
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([2, 2, 2, 2])

class OrangeRicky(tetramino):

    def __init__(self, numericX, numericY):
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 0, 0, 4], [0, 4, 4, 4]])

class BlueRicky(tetramino):

    def __init__(self, numericX, numericY):
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[3, 0, 0, 0], [3, 3, 3, 0]])

class Teewee(tetramino):

    def __init__(self, numericX, numericY):
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 0, 7, 0], [0, 7, 7, 7]])

class Cleverland(tetramino):

    def __init__(self, numericX, numericY):
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 8, 8, 0], [0, 0, 8, 8]])

class RhodeIsland(tetramino):

    def __init__(self, numericX, numericY):
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 6, 6, 0], [6, 6, 0, 0]])

class SmashBoy(tetramino):

    def __init__(self, numericX, numericY):
        self.x = numericX
        self.y = numericY
        self.numericImage = np.matrix([[0, 5, 5, 0], [0, 5, 5, 0]])


def draw(field, startx, starty, screen):
    for i in range(len(field)):
            for j in range(np.size(field, 1)): 
                if field[i , j]:
                   p = pygame.Rect( startx + 25 * j, starty + 25 * i, 25, 25)
                   pygame.draw.rect(screen, color[int(field[i , j])], p)


def isFull(array):
    for i in array:
        if not i:
            return False
    
    return True

def ceck(field, punti):
    eliminate = 0
    for i in range(len(field)):
            if  isFull(field[i]):
                field = np.delete(field,i,0)
                field = np.insert(field,0, 0, axis = 0)
                eliminate +=1

    if eliminate > 0:
        punti += pow(eliminate,eliminate)
        
    return (field, punti)   


def restart():
    return np.zeros( (28, 12) )            


def main():

    pygame.init()
    font = pygame.font.SysFont("freesansbold.ttf", 50)
    
    size = width, height = 25*14, 720
    black = 0, 0, 0
    blue = 42, 12, 240
    white = 255, 255, 255
    field = np.zeros( (28, 12) )
    fall_time = 0
    fall_speed = 0.27
    move_time = 0

    punti = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    downBar = pygame.Rect(0,height - 25, 25 * 14, 25)
    sideleft = pygame.Rect(0, height - 25 * 25, 25, height - 120)
    sideRight = pygame.Rect(25 * 13, height - 25 * 25, 25, height - 120)
    hero = Hero(4, 1)
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
            (field, punti) = ceck(field,punti)
            tetramino = copy.copy(tetramini[randint(0,6)])
            if not tetramino.fit(field):
                tetramino = None
            else:
                punti +=1
            nxt = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s and tetramino:
                fall_speed = 0.14
            else:
                fall_speed = 0.27

            if event.key == pygame.K_d and tetramino and move_time > fall_speed*1000:
                move_time = 0
                tetramino.goRight(field)
            elif event.key == pygame.K_a and tetramino and move_time > fall_speed*1000: 
                move_time = 0
                tetramino.goLeft(field)
            elif event.key == pygame.K_SPACE and tetramino and move_time > fall_speed*1000:
                move_time = 0
                tetramino.rotate(field)
            elif event.key == pygame.K_r:
                tetramino = None
                nxt = True
                punti = 0
                field = restart()


        screen.fill(black)

        fall_time += clock.get_rawtime() + punti/(100+punti)
        move_time += clock.get_rawtime()
        clock.tick()
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            if tetramino:
                nxt = tetramino.goDown(field)

        print(field)
        txtpt = "punti:" + str(punti)
        txtpt2 = "'r' per ricominciare"
        text = font.render(txtpt, False, white)
        text2 = font.render(txtpt2, False, white)
        draw(field, 25, 0, screen)
        screen.blit(text,(10,10))
        screen.blit(text2,(10,50))
        pygame.draw.rect(screen, white, downBar)
        pygame.draw.rect(screen, white, sideleft)
        pygame.draw.rect(screen, white, sideRight)
        pygame.display.flip()




if __name__=="__main__":
    main()

