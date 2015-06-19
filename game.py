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
    gears.append(Gear(bound,fixed=True))
    gears[0].setPosition(100, 100)
    selGear = None
    while 1:
        screen.fill(pygame.Color("black"))
        dt = clock.tick(60)
        time += dt
        # process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.dict['key'] in [pygame.K_q,pygame.K_ESCAPE,pygame.K_BREAK]:
                    sys.exit()
                if event.dict['key'] == pygame.K_r:
                    newGear = Gear(bound, 
                                color=pygame.Color(random.randint(0,255),
                                            random.randint(0,255),
                                            random.randint(1,254)))
                    gears.append(newGear)
            if event.type == pygame.MOUSEBUTTONDOWN:
                ox, oy = pygame.mouse.get_pos()
                #find gear mouse is over
                g = mouse.collidelist([g.pos for g in gears[1:]])
                if g != -1:
                    selGear = gears[g+1]
            if event.type == pygame.MOUSEBUTTONUP:
                selGear = None
            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                mouse.center = mx,my
                if selGear and not selGear.fixed:
                    selGear.setPosition(selGear.x + mx - ox, selGear.y + my - oy)
                    ox, oy = mx, my
                    
        # draw items
        for g in gears:
            g.update(dt)
            g.draw(screen)
            g.w=0
            
        # drive the gears
        drive(10,gears[0],gears[1:])
        
        # update the display
        pygame.display.flip()
        
def drive(w, driveGear, gears):
    driveGear.w = w

    for i,g in enumerate(gears):
        if(((driveGear.x-g.x)**2+(driveGear.y-g.y)**2)**0.5 <= driveGear.r+g.r):
            drive(-driveGear.w, g, gears[:i]+gears[i+1:])
            
if __name__ == "__main__":
    main()