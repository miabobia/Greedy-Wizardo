import pygame
from animate import Animate
"""
object should have attributes:
    PARAMETERS:
        - x
        - y
        - w
        - h
        - list of animation cycles eg (idle, run ..)
    spr_obj (pygame.sprite object)
"""

class Base:

    def __init__(self, x, y, w, h, anim_cycles):
        #sprites will be scaled to size w x hs

        #init parameters
        self.x, self.y = x, y
        self.w, self.h = w, h

        #how anim_cycles is formatted
        # [([spr1,spr2,...], [(frame_len, spr_index), ...]), ]
        self.anim_cycles = anim_cycles
        #making animation object
        self.anim = Animate(self.anim_cycles[0][0],self.anim_cycles[0][1])

        #getting first image
        self.spr_str = self.anim_cycles[0][0][0] 
        self.spr_obj = pygame.image.load("sprites\\" + self.spr_str)

        #scaling sprite image to be (w x h) dimensions
        self.spr_obj = pygame.transform.scale(self.spr_obj, (self.w,self.h))

    def show(self, screen):
        pygame.draw.rect(screen, (230, 170, 210),pygame.Rect(self.x, self.y, self.w, self.h))
        screen.blit(self.spr_obj, (self.x, self.y))
    
    def update_anim(self):
        #calling this updates the animation object
        #it returns the path to sprite according to animation timings
        spr_str = self.anim.update()

        #if our next frame's sprite does not match with current frame
        if self.spr_str != spr_str:
            #reconstruct spr_obj variable using new spr_str
            self.spr_obj = pygame.image.load("sprites\\" + spr_str)

            #scale new sprite
            self.spr_obj = pygame.transform.scale(self.spr_obj, (self.w,self.h))

            self.spr_str = spr_str






