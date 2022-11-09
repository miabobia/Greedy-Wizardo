from base_object import Base
import pygame

class Projectile(Base):

    released = False
    target = (None,None)
    #z-axis value. as z approaches 0 that means it is getting closer to the ground
    z = 100

    def __init__(self, x, y, w, h, anim_cycles):
        super().__init__(x, y, w, h, anim_cycles)

    def update(self, mx, my):
        if self.released:
            self.z -= 1
            if self.z <= 0:
                self.released = False
                self.z = 100
        else:
            self.x,self.y = mx,my

    def show(self,screen,d=0):
        if self.released:
            color = (116,109,101)
            pygame.draw.circle(screen, color, (self.x, self.y),self.z)
        else:
            color = (219,100,20)
            #drawing crosshair
            pygame.draw.circle(screen, color, (self.x, self.y),self.z,1)
    


    def release(self):
        self.released = True




