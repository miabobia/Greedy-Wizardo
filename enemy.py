from base_object import Base
from random import randint
import funcs
class Enemy(Base):
    #enemies will generate a path. paths go from level to level going down
    #if two enemies try to occupy the same bush the new enemy will kick out the old enemy
    #

    path = []
    target_bush = None
    path_ind = 0
    hiding   = False
    
    def __init__(self, x, y, w, h, anim_cycles,bushes):
        super().__init__(x, y, w, h, anim_cycles)
        #pass in list of all bushes in game
        self.bushes = bushes
        self.get_path()
        self.print_path()
        self.target_bush = self.path[self.path_ind]

    def update(self):
        self.update_anim()
        #getting target_bush position
        # bx,by = self.target_bush.get_pos()
        if not self.hiding:
            mov_vec = self.target_bush.get_pos()
            mov_vec = funcs.get_normal_vector(mov_vec)
            self.x += mov_vec[0]
            self.y += mov_vec[1]
            if funcs.rect_collide(self.x,self.y,self.w,self.h, \
                self.target_bush.x, self.target_bush.y, self.target_bush.w, self.target_bush.h):
                    self.hiding = True
        # x,y = self.spr_obj.get_size()
        # print("X:{} Y:{}".format(x,y))

    def get_path(self):
        for i in range(5):
            self.path.append(self.get_bush(i))
    
    def get_bush(self,level,lock=-1):
        lvl_bushes = []
        for i in range(len(self.bushes)):
            if self.bushes[i].get_level() == level and lock != i:
                lvl_bushes.append(i)
        #return bushes[randint(0,len(bushes))]
        # return randint(0,len(lvl_bushes))
        r = randint(0,len(lvl_bushes)-1)
        # return lvl_bushes[r]
        return self.bushes[lvl_bushes[r]]

    def print_path(self):
        for p in self.path:
            print(p,end=' ')
        print()