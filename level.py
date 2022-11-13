from random import randint
from enemy import Enemy
import header as hd
from projectile import Projectile
import pygame
import funcs

"""
PARAMETERS:
 - Enemy Info (e_info) -> [(# of enemies, type of enemy), ...]
 - Bushes

"""


class Level:

    enemies = []
    e_timer = 0


    def __init__(self, bushes, e_info,screen):
        print("level created")
        self.enemy_delay = 100
        self.bushes = bushes
        self.e_info = e_info
        self.screen = screen
        self.projectile = self.spawn_projectile()

    def update(self):

        self.e_timer += 1
        if self.e_timer >= self.enemy_delay and self.e_info:
            self.e_timer = 0
            self.spawn_enemy()
            self.enemy_delay = randint(50,150)

        for b in self.bushes:
            b.update()


        for e in self.enemies:
            e.update()

        mx,my = pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
        self.projectile.update(mx,my)
        if self.projectile.hitting:
            #check if colliding with enemies

            for e in self.enemies:
                if e.get_hiding():
                    continue
                r1 = [self.projectile.x, self.projectile.y, self.projectile.w, self.projectile.h]
                r2 = [e.hb[0], e.hb[1], e.hb[2], e.hb[3]]

                if funcs.rect_collide(r1[0],r1[1],r1[2],r1[3], r2[0],r2[1],r2[2],r2[3]):
                    self.remove_enemy(e)

            self.projectile.reset()

        #level complete condition
        if not self.e_info and not self.enemies:
            print("LEVEL IS FINISHED")

    def show(self):
        for b in self.bushes:
            b.show(self.screen)

        for e in self.enemies:
            e.show(self.screen,debug=1)
    
        self.projectile.show(self.screen,d=1)
    def spawn_enemy(self):
        e_type = self.get_enemy()
        if e_type:
            self.enemies.append(e_type(0,0,100,100,[hd.ENEMY_RUN],self.bushes))
        
    def get_enemy(self):
        #returns an enemy type and 
        # decrements the amt of those enemy types in e_info
        choice = randint(0,len(self.e_info)-1)
        e_count = self.e_info[choice][0]-1
        return_type = self.e_info[choice][1]
        if e_count == 0:
            self.e_info.remove(self.e_info[choice]) #removing enemy type from list if we are adding in last enemy
        else:    
            self.e_info[choice] = (e_count, return_type)
        return return_type

    def spawn_projectile(self):
        return Projectile(10,10,1,[hd.BUSH_IDLE])

    def release_projectile(self):
        self.projectile.release()

    def remove_enemy(self, e):
        self.enemies.remove(e)