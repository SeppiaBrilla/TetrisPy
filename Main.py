#!/usr/bin/env python3

import pygame
import sys
import time
from random import randint



class tetramino:
    def __init__(self, startX, startY):
        self.image = []
        self.numericImage = []
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.y= 0
        self.x = 5


    def draw(self, screen):
        white = 255, 255, 255
        for rect in self.image:
            pygame.draw.rect(screen, white, rect)

    def goDown(self,height, field):
        for rect in self.image:
            (x, y) = rect.midbottom
            if y >= height - 24 or self.stopd:
                self.stopd = True
                return  True       

        for rect in self.image:
            (x, y) = rect.midbottom       
            rect.move_ip([0,25])

        self.y +=1
        for point in self.numericImage:
            (x, y) = point
            field[self.y + y - 1][self.x + x] = 0
            field[self.y + y][self.x + x] = 1

    def goRight(self, width, field):
        for rect in self.image:
            (x, y) = rect.midright
            if x >= width - 24 or self.stopr:
                self.stopr = True    
                return

        for rect in self.image:
            (x, y) = rect.midright                
            rect.move_ip([25,0])

        self.x +=1
        for point in self.numericImage:
            (x, y) = point
            
            field[self.y + y][self.x + x - 1] = 0
            field[self.y + y][self.x + x] = 1

        self.stopl = False

    def goLeft(self, width, field):
        for rect in self.image:
            (x, y) = rect.midleft
            if x <= width + 25 or self.stopl:
                self.stopl = True    
                return

        for rect in self.image:
            (x, y) = rect.midright                
            rect.move_ip([-25,0])

        self.x -= 1
        for point in self.numericImage:
            (x, y) = point
            
            field[self.y + y][self.x + x + 1] = 0
            field[self.y + y][self.x + x] = 1

        self.stopr = False
    
    def rotate(self, field):
        for n in range(len(self.numericImage)):
           (x, y) = self.numericImage[n]  
           print(self.numericImage[n])       
           field[self.y + y][self.x + x] = 0
           self.numericImage[n] = (y, x)
           print(self.numericImage[n])
        
        for rect in self.image:
            rect.centerx, rect.centery = rect.centery, rect.centerx
        
        


class Hero(tetramino):

    def __init__(self, startX, startY, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.image = []
        self.x = numericX
        self.y = numericY
        self.numericImage = [[0 , 3], [0, 2], [0, 1], [0, 0]]
        square = pygame.Rect(startX, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX, startY + 25, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX, startY + 50, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX, startY + 75, 25, 25)
        self.image.append(square)


class OrangeRicky(tetramino):

    def __init__(self, startX, startY, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.image = []
        self.x = numericX
        self.y = numericY
        self.numericImage = [[0 , 0], [1, 0], [2, 0], [2, -1]]
        square = pygame.Rect(startX, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 50, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 50, startY -25, 25, 25)
        self.image.append(square)

class BlueRicky(tetramino):

    def __init__(self, startX, startY, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.image = []
        self.x = numericX
        self.y = numericY
        self.numericImage = [[0 , 0], [0, -1], [1, 0], [2, 0]]
        square = pygame.Rect(startX, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX, startY - 25, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 50, startY, 25, 25)
        self.image.append(square)

class Teewee(tetramino):

    def __init__(self, startX, startY, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.image = []
        self.x = numericX
        self.y = numericY
        self.numericImage = [[0 , 0], [1, 0], [1, -1], [2, 0]]
        square = pygame.Rect(startX, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY - 25, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 50, startY, 25, 25)
        self.image.append(square)

class Cleverland(tetramino):

    def __init__(self, startX, startY, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.image = []
        self.x = numericX
        self.y = numericY
        self.numericImage = [[2 , 1], [1, 1], [1, 0], [0, 0]]
        square = pygame.Rect(startX + 50, startY + 25, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY + 25, 25, 25)
        self.image.append(square)

class RhodeIsland(tetramino):

    def __init__(self, startX, startY, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.image = []
        self.x = numericX
        self.y = numericY
        self.numericImage = [[0 , 0], [1, 0], [1, -1], [2, -1]]
        square = pygame.Rect(startX, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY - 25, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 50, startY - 25, 25, 25)
        self.image.append(square)

class SmashBoy(tetramino):

    def __init__(self, startX, startY, numericX, numericY):
        self.stopd = False
        self.stopr = False
        self.stopl = False
        self.image = []
        self.x = numericX
        self.y = numericY
        self.numericImage = [[1 , 1], [0, 1], [1, 0], [0, 0]]
        square = pygame.Rect(startX + 25, startY + 25, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX + 25, startY, 25, 25)
        self.image.append(square)
        square = pygame.Rect(startX, startY + 25, 25, 25)
        self.image.append(square)

def main():
    
    size = width, height = 1280, 720
    speed = [1, 1]
    black = 0, 0, 0
    blue = 42, 12, 240
    white = 255, 255, 255
    field = [[0 for x in range(10)] for y in range(28)]
    clock = pygame.time.Clock() #10 x 40
    screen = pygame.display.set_mode(size)
    downBar = pygame.Rect(0,height - 25, 25 * 13, 25)
    sideleft = pygame.Rect(0, height - 25 * 25, 25, height - 120)
    sideRight = pygame.Rect(25 * 12, height - 25 * 25, 25, height - 120)
    hero = Hero( 25 * 6, height - 25 * 25, 4, 4)
    orangeRicky = OrangeRicky(25 * 6, height - 25 * 24, 4, 5)
    blueRicky = BlueRicky(25 * 6, height - 25 * 24, 4, 5)
    teewee = Teewee(25 * 6, height - 25 * 24, 4, 5)
    cleverland = Cleverland(25 * 6, height - 25 * 24, 4, 5)
    rhodeIsland = RhodeIsland(25 * 6, height - 25 * 24, 4, 5)
    smashboy = SmashBoy(25 * 6, height - 25 * 24, 4, 5)
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
            tetramino.goRight(25 * 12, field)
        elif pressed[pygame.K_a]:
            tetramino.goLeft(0, field)
        elif pressed[pygame.K_SPACE]:
            tetramino.rotate(field)


        screen.fill(black)
        tetramino.draw(screen)
        nxt = tetramino.goDown(height - 25, field)
        pygame.draw.rect(screen, white, downBar)
        pygame.draw.rect(screen, white, sideleft)
        pygame.draw.rect(screen, white, sideRight)
        pygame.display.flip()
        time.sleep(0.25)




if __name__=="__main__":
    main()

