import pygame
from pygame.locals import *

import sys

from bush import Bush
from enemy import Enemy
from projectile import Projectile

import header as hd

from level import Level

#pygame boilerplate
width, height =  hd.WIDTH, hd.HEIGHT
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

projectiles = []

l = None



def main():
    global l

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

    #creating enemies

    l = Level(bushes, hd.E_INFO, screen)

    # enemies.append(Enemy(0,0,100,100,enemy_a,bushes))


    # projectiles.append(Projectile(100,100,50,50,bush_a))

    dt = 1/60

    while True:
        update(dt)
        draw(screen)

def update(dt):
    global l

    mx,my = pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            l.release_projectile()
        
    # for b in bushes:
    #     b.update()

    # for e in enemies:
    #     e.update()

    l.update()


    # for p in projectiles:
    #     p.update(mx,my)

    clock.tick(60)

def draw(screen):
    global l
    screen.fill((255, 200, 250)) #pink
    
    # for b in bushes:
    #     b.show(screen,1)
    #     b.show_level(screen,font)

    # for e in enemies:
    #     e.show(screen,1)

    l.show()

    for p in projectiles:
        p.show(screen)
   
    screen.blit(update_fps(),(10,0))

    pygame.display.flip()

def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text


main()