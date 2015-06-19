import pygame
import math
class Gear:
    def __init__(self, bound, color=pygame.Color("white"), teeth=16, mass=10):
        self.color = color
        self.t = teeth
        self.m = mass
        self.w = .1
        
        p = 2 * self.t
        self.r = int((p * self.t) / (2 * math.pi))
        
        # create image surface
        self.image = pygame.Surface((self.r*2,self.r*2))
        #self.image.set_colorkey(pygame.Color("magenta"))
        self.image.fill(pygame.Color("magenta"))
        self.rect = self.image.get_rect()
        
        self.degree = 0
        
        # create rectangles
        self.pos = pygame.Rect(0, 0, self.r, self.r)
        toDraw = pygame.Rect(0,0, self.r, self.r)
        toDraw.center = self.rect.center
        
        # draw onto the image
        pygame.draw.rect(self.image, self.color, toDraw)
        self.rotimage = self.image
        
        # move gear
        self.setPosition(bound.center[0],bound.center[1])

    def draw(self, screen):
        screen.blit(self.rotimage, self.rect)
        
    def update(self,dt):
        oldrect = self.rect
        self.rotimage = pygame.transform.rotate(self.image, self.degree)
        self.rect = self.rotimage.get_rect()
        self.rect.center = oldrect.center
        self.degree += self.w * dt
        
        if self.degree > 360:
            self.degree = 0

        
    def setPosition(self,newx,newy):
        self.pos.center = newx,newy
        self.rect.center = newx,newy
        self.x, self.y = self.pos.center
