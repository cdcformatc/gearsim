import pygame
import math
import os
class Gear:
    def __init__(self, bound, fixed=False, color=pygame.Color("white"), teeth=12, mass=10):
        self.fixed = fixed
        self.color = color
        self.t = teeth
        self.m = mass
        self.w = 0
        self.degree = 0
        
        self.r = int((2*self.t * self.t) / (2 * math.pi))
        
        # create image surface
        self.image = pygame.Surface((2*self.r,2*self.r))
        self.image.set_colorkey(pygame.Color("magenta"))
        self.image.fill(pygame.Color("magenta"))

        gearsurf = pygame.image.load(os.path.join(os.getcwd(), 'images', 'run.png'))
        gearsurf = pygame.transform.scale(gearsurf, (2*self.r,2*self.r))
        self.rect = gearsurf.get_rect()
        
        self.image.blit(gearsurf, self.rect)
        self.rotimage = self.image
        
        # create rectangles
        self.pos = pygame.Rect(0, 0, 2*self.r, 2*self.r)

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
        
