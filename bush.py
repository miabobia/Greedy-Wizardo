from base_object import Base
import pygame
class Bush(Base):
    
    def __init__(self, x, y, w, h, anim_cycles, level,i):
        super().__init__(x, y, w, h, anim_cycles)
        self.level = level
        self.i = i

    def update(self):
        self.update_anim()
        # x,y = self.spr_obj.get_size()
        # print("X:{} Y:{}".format(x,y))

    def show_level(self,screen,font):


        fps_text = font.render(str(self.level), 1, pygame.Color("coral"))
        # screen.blit()
        screen.blit(fps_text,(self.x,self.y-10))
        fps_text = font.render(str(self.i), 1, pygame.Color("coral"))
        # screen.blit()
        screen.blit(fps_text,(self.x+20,self.y-10))
    
    def get_level(self):
        return self.level