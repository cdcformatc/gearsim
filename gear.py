import pygame
import math
import os
class Gear:
    def __init__(self, bound, color=pygame.Color("white"), teeth=16, mass=10):
        self.color = color
        self.t = teeth
        self.m = mass
        self.w = 10
        self.degree = 0
        
        p = 2 * self.t
        self.r = int((p * self.t) / (2 * math.pi))
        
        # create image surface
        self.image = pygame.Surface((self.r,self.r))
        self.image.set_colorkey(pygame.Color("magenta"))
        self.image.fill(pygame.Color("magenta"))

        gearsurf = pygame.image.load(os.path.join(os.getcwd(), 'images', 'run.png'))
        gearsurf = pygame.transform.scale(gearsurf, (self.r,self.r))
        self.rect = gearsurf.get_rect()
        self.rect.center = self.image.get_rect().center
        
        self.image.blit(gearsurf, self.rect)
        self.rotimage = self.image
        
        # create rectangles
        self.pos = pygame.Rect(0, 0, self.r, self.r)

        # move gear
        self.setPosition(bound.center[0],bound.center[1])

    def draw(self, screen):
        screen.blit(self.rotimage, self.rect)
        
    def update(self,dt):
        oldrect = self.rect
        self.rotimage = pygame.transform.rotate(self.image, self.degree)
        self.rect = self.rotimage.get_rect()
        self.rect.center = oldrect.center
        self.degree += self.w * dt/1000.0
        
        
    def setPosition(self,newx,newy):
        self.pos.center = newx,newy
        self.rect.center = newx,newy
        self.x, self.y = self.pos.center
