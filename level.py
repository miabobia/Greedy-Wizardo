from random import randint
from enemy import Enemy
import header as hd
from projectile import Projectile

"""
PARAMETERS:
 - Enemy Info (e_info) -> [(# of enemies, type of enemy), ...]
 - Bushes

"""


class Level:

    enemies = []
    e_timer = 0

    projectiles = []

    def __init__(self, bushes, e_info,screen):
        print("level created")
        self.enemy_delay = 100
        self.bushes = bushes
        self.e_info = e_info
        self.screen = screen

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
        for p in self.projectiles:
            p.update(mx,my)


    
        

        #level complete condition
        if not self.e_info and not self.enemies:
            print("LEVEL IS FINISHED")

    def show(self):
        for b in self.bushes:
            b.show(self.screen)

        for e in self.enemies:
            e.show(self.screen)
    
        for p in self.projectiles:
            p.show()

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
        self.projectiles.append(1,1,hd.bush_a)
        pass
