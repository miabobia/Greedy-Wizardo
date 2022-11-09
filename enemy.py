from base_object import Base
from random import randint
import funcs

class Enemy(Base):
    #enemies will generate a path. paths go from level to level going down
    #if two enemies try th0[0],h0[1],h0[2],h0[3]o occupy the same bush the new enemy will kick out the old enemy
    #

    path = []
    hiding = False
    target_bush = None #bush being targetted by enemy
    level = -1 #what level of path enemy is currently selecting/occupying
    mov_vec = None #normal vector to be added to x,y to move
    spd = 1

    
    def __init__(self, x, y, w, h, anim_cycles,bushes):
        super().__init__(x, y, w, h, anim_cycles)
        self.bushes = bushes
        self.get_path()
        # self.print_path()
        # self.target_bush = self.path[0]
        self.new_target_bush()

        print("TARGET BUSH LEVEL: ",self.target_bush.i)

    def update(self):
        self.update_anim()
        if not self.hiding:
            self.x += self.mov_vec[0]
            self.y += self.mov_vec[1]
            self.update_hitbox()

            h0,h1 = self.get_hitbox(),self.target_bush.get_hitbox() #making more readable

            if funcs.rect_collide(h0[0],h0[1],h0[2],h0[3],h1[0],h1[1],h1[2],h1[3]):
                self.hiding = True
                self.target_bush.update_animation(1)

                #DEBUG SHIT
                self.spd += 1
                self.hiding = False
                self.new_target_bush(self.spd)




    def get_path(self):
        for i in range(5):
            self.path.append(self.get_bush(i))
    
    def get_bush(self,level,lock=-1):
        #returns a random bush at 'level'
        #if lock is passed bushes[i] cannot be returned
        lvl_bushes = []
        for i in range(len(self.bushes)):
            if self.bushes[i].get_level() == level and lock != i:
                lvl_bushes.append(self.bushes[i])

        r = randint(0,len(lvl_bushes)-1)
        return lvl_bushes[r]

    def new_target_bush(self,spd=1):
        #targetting bush a level down
        self.level += 1
        self.target_bush = self.path[self.level]

        #setting mov_vec
        ep = self.get_pos_vec()
        bp = self.target_bush.get_pos_vec()
        f = funcs.get_vector(ep[0],ep[1], bp[0],bp[1])
        self.mov_vec = funcs.get_normal_vector(f)
        self.mov_vec = (self.mov_vec[0]*spd, self.mov_vec[1]*spd)

    def print_path(self):
        for p in self.path:
            print(p,end=' ')
        print()