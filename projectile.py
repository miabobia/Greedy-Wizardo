from base_object import Base
import pygame
import header 

class Projectile(Base):

    released = False
    target = (None,None)
    #z-axis value. as z approaches 0 that means it is getting closer to the ground
    z = 100
    hitting = False #if projectile has reached teh ground

    def __init__(self, w, h, speed, anim_cycles):
        super().__init__(1, 1, w, h, anim_cycles)
        self.speed = speed

    def update(self, mx, my):
        self.update_hitbox()
        if self.released:
            self.z -= self.speed
            if self.z <= 0:
                self.hitting = True
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

            color = (116,109,101)
            pygame.draw.circle(screen, color, (header.WIDTH - header.WIDTH/3, header.HEIGHT - header.HEIGHT/4),self.z)
    
        if d:
            self.show_inside_hitbox(screen)

        print("X: ",self.x)
        print("Y: ",self.y)
        print()


    def release(self):
        self.released = True

    def reset(self):
        self.z = 100
        self.released = False
        self.hitting = False




