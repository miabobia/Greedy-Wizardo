import pygame
from animate import Animate
import funcs
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

    hb = None #hb is the center rectangle used for calculating hitboxes

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

        self.update_hitbox()



    def show(self, screen, debug=0):
        screen.blit(self.spr_obj, (self.x, self.y))
        if debug:
            self.show_rect(screen, pygame.Rect(self.x, self.y, self.w, self.h)) #outside hitbox
            self.show_inside_hitbox(screen)

    def show_inside_hitbox(self,screen):
        self.show_rect(screen,pygame.Rect(self.hb[0],self.hb[1],self.hb[2],self.hb[3])) #drawing self.hitbox attribute

    def show_rect(self,screen,rect):
        #takes a rect hitbox and draws rectangle border to show hitbox
        color = (255,0,0)
        pygame.draw.rect(screen, color, rect,  2)

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

    def update_hitbox(self):
        #updating self.hb attrib
        #enemy needs to update its hitbox, bushes DO NOT
        self.hb = funcs.get_center_rect(self.x,self.y,self.w,self.h,0.5)


    def get_pos_vec(self):
        return (self.x,self.y)

    def get_hitbox(self):
        return self.hb
    
    def update_animation(self,n):
        self.anim.set_f_names(self.anim_cycles[n][0])
        self.anim.set_order(self.anim_cycles[n][1])
    # #getting first image
    # self.spr_str = self.anim_cycles[0][0][0] 
    # self.spr_obj = pygame.image.load("sprites\\" + self.spr_str)

    # #scaling sprite image to be (w x h) dimensions
    # self.spr_obj = pygame.transform.scale(self.spr_obj, (self.w,self.h))







