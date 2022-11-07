from base_object import Base
from random import randint
class Enemy(Base):
    #enemies will generate a path. paths go from level to level going down
    #if two enemies try to occupy the same bush the new enemy will kick out the old enemy
    #

    path = []
    
    def __init__(self, x, y, w, h, anim_cycles,bushes):
        super().__init__(x, y, w, h, anim_cycles)
        self.bushes = bushes
        self.get_path()
        self.print_path()

    def update(self):
        self.update_anim()
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
        return lvl_bushes[r]

    def print_path(self):
        for p in self.path:
            print(p,end=' ')
        print()