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
        
        self.rect = pygame.Rect(0,0,self.r,self.r)        
        self.setPosition(bound.center[0],bound.center[1])
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.r)
        
    def setPosition(self,newx,newy):
        self.rect.center = newx,newy
        self.x,self.y = self.rect.center
