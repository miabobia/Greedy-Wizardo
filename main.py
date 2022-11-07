import pygame
from pygame.locals import *

import sys

from bush import Bush
from enemy import Enemy

import header as hd

#pygame boilerplate
width, height =  720,960
screen = pygame.display.set_mode((width, height))

# a = [(["bush.png","bounce2.png","bounce3.png"],[(30,0),(5,1),(10,2),(5,1)])]
bush_a = [hd.BUSH_IDLE, hd.BUSH_OCCUPY]
enemy_a = [hd.ENEMY_RUN]

pygame.init()
#TEST CODE
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial",18)

#OBJECT LISTS
bushes  = []
enemies = []


def main():

    #creating bushes
    level = 0 #bushes are seperated by levels (of height) 0 at top screen n at bottom
    i = -1
    r_ind = 0    #index for rows
    rows = [2,1] #bushes go in rows of 2 and 1
    j = 0
    for b in hd.bush_crds:
        i+=1
        if i == rows[r_ind]:
            r_ind += 1
            i = 0
            if r_ind > len(rows)-1: r_ind = 0
            level += 1
        
        bushes.append(Bush(b[0], b[1], hd.BUSH_WIDTH, hd.BUSH_HEIGHT, bush_a, level,j))
        j+=1

    enemies.append(Enemy(0,0,10,10,enemy_a,bushes))

    dt = 1/60

    while True:
        update(dt)
        draw(screen)

def update(dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for b in bushes:
        b.update()

    clock.tick(60)

def draw(screen):
    screen.fill((255, 200, 250)) #pink
    
    for b in bushes:
        b.show(screen)
        b.show_level(screen,font)

    screen.blit(update_fps(),(10,0))

    pygame.display.flip()

def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text


main()