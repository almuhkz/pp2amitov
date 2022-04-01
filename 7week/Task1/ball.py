import pygame

pygame.init()
screen_h = 700
screen_w = 700
screen = pygame.display.set_mode((screen_h,screen_w))
done = False
x = 50
y = 50
pygame.display.set_caption("Ball")
white = (255,255,255)
red = (255,0,0)
radius = 25
px = 30
clock = pygame.time.Clock()
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]: y -= px
        if pressed[pygame.K_DOWN]: y += px
        if pressed[pygame.K_LEFT]: x -= px
        if pressed[pygame.K_RIGHT]: x += px
        if x < radius: x = radius
        if y < radius: y = radius
        if x > screen_w-radius: x = screen_w-radius
        if y > screen_w-radius: y = screen_h-radius

        color = (255, 100, 0)

        screen.fill(white)

        pygame.draw.circle(screen, red,(x,y),radius)

        pygame.display.flip()
        clock.tick(60)
