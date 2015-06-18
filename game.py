import pygame
import os
import sys

from gear import Gear

os.environ['SDL_VIDEO_CENTERED'] = '1'

#admin settings
FIELD_SIZE=900

def read_keyboard():
    x = pygame.key.get_pressed()
    # if x[pygame.K_UP]:
    # if x[pygame.K_DOWN]:
    # if x[pygame.K_RIGHT]:
    # if x[pygame.K_LEFT]:
    if x[pygame.K_ESCAPE] or x[pygame.K_q] or x[pygame.K_BREAK]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    return x

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
        read_keyboard()
        dt = clock.tick(60)
        time += dt
        
        # process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ox, oy = pygame.mouse.get_pos()
                #find gear mouse is over
                
                g = mouse.collidelist([g.rect for g in gears])
                if g != -1:
                    selGear = gears[g]
            if event.type == pygame.MOUSEBUTTONUP:
                selGear = None
            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                mouse.center = mx,my
                if selGear:
                    selGear.setPosition(selGear.x + mx - ox, selGear.y + my - oy)
                    ox, oy = mx, my
        # draw items
        for g in gears:
            g.update(dt)
            g.draw(screen)
            
        pygame.display.flip()
        
if __name__ == "__main__":
    main()