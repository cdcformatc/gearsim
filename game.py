import pygame
import os
import sys
import random

from gear import Gear

os.environ['SDL_VIDEO_CENTERED'] = '1'

#admin settings
FIELD_SIZE=900

def main():
    pygame.init()
    clock = pygame.time.Clock()
    size = width, height = FIELD_SIZE,FIELD_SIZE
    screen = pygame.display.set_mode(size)
    bound = screen.get_rect()
    gears = []
    time = 0
    mouse = pygame.Rect(pygame.mouse.get_pos(),(1,1))
    gears.append(Gear(bound))
    selGear = None
    
    while 1:
        screen.fill(pygame.Color("black"))
        dt = clock.tick(60)
        time += dt
        
        # process events
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.dict['key'] in [pygame.K_q,pygame.K_ESCAPE,pygame.K_BREAK]:
                    sys.exit()
                if event.dict['key'] == pygame.K_r:
                    gears.append(Gear(bound,pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))))
            if event.type == pygame.MOUSEBUTTONDOWN:
                #find gear mouse is over
                selGear = gears[mouse.collidelist([g.rect for g in gears])]
                ox, oy = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                selGear = None
            if event.type == pygame.MOUSEMOTION:
                if selGear:
                    mx, my = pygame.mouse.get_pos()
                    selGear.setPosition(selGear.x + mx - ox, selGear.y + my - oy)
                    ox, oy = mx, my
        # draw items
        for g in gears:
            g.update(dt)
            g.draw(screen)
            
        pygame.display.flip()
        
if __name__ == "__main__":
    main()