import pygame
pygame.init()
screen_h = 700
screen_w = 700
screen = pygame.display.set_mode((screen_h,screen_w))
pygame.mixer.music.load('C:\\Users\\amito\\OneDrive\\Documents\\PP2\\7week\\Task1\\1.mp3')
volume = 1
done = False
paused =False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            '''if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.mixer.music.play(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    pygame.mixer.music.pause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    pygame.mixer.music.pause()'''
            p_pressed = pygame.key.get_pressed()[pygame.K_p]
            #space_pressed = pygame.key.get_pressed()[pygame.K_SPACE]
            space_pressed = False
            if(p_pressed): pygame.mixer.music.play(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                pygame.mixer.music.unpause()

    screen.fill((255,255,255))
    pygame.display.flip()
    clock.tick(60)