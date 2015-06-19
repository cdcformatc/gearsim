import pygame
import math
class Gear:
    def __init__(self, bound, color=pygame.Color("white"), teeth=16, mass=10):
        self.color = color
        self.t = teeth
        self.m = mass
        self.w = 0
        
        p = 2 * self.t
        self.r = int((p * self.t) / (2 * math.pi))
        
        # create image surface
        self.image = pygame.Surface((self.r*2,self.r*2))
        self.image.set_colorkey(pygame.Color("magenta"))
        self.image.fill(pygame.Color("magenta"))
        self.rect = self.image.get_rect()
        
        # create rectangles
        self.pos = pygame.Rect(0, 0, self.r, self.r)
        toDraw = pygame.Rect(self.imagerect.left+self.r/2, self.imagerect.top+self.r/2, self.r, self.r)
        
        # draw onto the image
        pygame.draw.rect(self.image, self.color, toDraw)
        
        # move gear
        self.setPosition(bound.center[0],bound.center[1])

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self,dt):
        pass
        
    def setPosition(self,newx,newy):
        self.pos.center = newx,newy
        self.rect.center = newx,newy
        self.x, self.y = self.pos.center
