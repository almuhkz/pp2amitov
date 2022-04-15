import pygame
from pygame.locals import *
surface = pygame.display.set_mode((480, 320))
## Colors list
GREEN = (0, 255, 0)
GRAY = (197, 197, 197)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (107, 104, 99)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)
PURPLE = (167, 0, 238)
DARK_GREEN = (58, 158, 73)
WHITE = (255, 255, 255)
BROWN = (85, 46, 46)
PRETTY_BLUE = (0, 238, 195)

##
circle = pygame.image.load("img/circle.jpg")
square = pygame.image.load("img/square.jpg")
eraser = pygame.image.load("img/eraser.png")
rectangle = pygame.transform.scale(pygame.image.load("img/rectangle.jpg"), (40, 40))
triangle = pygame.transform.scale(pygame.image.load("img/triangle.jpg"), (40, 40))
r_triangle = pygame.transform.scale(pygame.image.load("img/rtriangle.jpg"), (40, 40))
rhombus = pygame.transform.scale(pygame.image.load("img/rhombus.jpg"), (40, 40))
circle_button_1 = pygame.transform.scale(circle, (40, 40))
circle_button_2 = pygame.transform.scale(square, (40, 40))
circle_rect = pygame.Rect(5, 120, 40, 40)
square_rect = pygame.Rect(47, 120, 40, 40)

stamp = "circle"
stamp_state = False

pygame.init()


## font setup
menu_font = pygame.font.Font("font/FreeSans.ttf", 9)
menu_text = menu_font.render("Almukhamed's Paint", True, BLACK)

clear_text = menu_font.render("  Clear", True, BLACK)
brush_text = menu_font.render("Brushes", True, BLACK)
tutorial_rec = menu_font.render("R - Rectangle", True, WHITE)
tutorial_tri = menu_font.render("T - Right Triangle", True, WHITE)
tutorial_rtri = menu_font.render("Y - Triangle", True, WHITE)
tutorial_rho = menu_font.render("D - Rhombus", True, WHITE)
save_text = menu_font.render("  SAVE", True, BLACK)



draw = False
brush_size = 5
brush_color = GREEN
menu_rect = pygame.Rect(0, 0, 100, 320)
screen_rect = pygame.Rect(100, 0, 380, 320)



green_rect = pygame.Rect(5, 55, 20, 20)
red_rect = pygame.Rect(27, 55, 20, 20)
blue_rect = pygame.Rect(49, 55, 20, 20)
pink_rect = pygame.Rect(71, 55, 20, 20)
light_blue_rect = pygame.Rect(5, 77, 20, 20)
yellow_rect = pygame.Rect(27, 77, 20, 20)
orange_rect = pygame.Rect(49, 77, 20, 20)
purple_rect = pygame.Rect(71, 77, 20, 20)
dark_green_rect = pygame.Rect(5, 99, 20, 20)
brown_rect = pygame.Rect(27, 99, 20, 20)
white_rect = pygame.Rect(49, 99, 20, 20)
pretty_blue_rect = pygame.Rect(71, 99, 20, 20)

clear_rect = pygame.Rect(10, 290, 70, 25)

eraser_rect = pygame.Rect(27, 210, 40, 40)

thin_brush = pygame.Rect(5, 185, 20, 20)
medium_brush = pygame.Rect(27, 185, 20, 20)
thick_brush = pygame.Rect(49, 185, 20, 20)
supa_brush = pygame.Rect(71, 185, 20, 20)


save_rect = pygame.Rect(5, 260, 90, 25)
save_flag = False
file_number = 1



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False
    
        
    # Drawing dot when mousebuttondown
    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100 and stamp_state == False:
        pygame.draw.circle(surface, brush_color, mouse_pos, brush_size)
        save_flag = False
    # Drawing stamp when mousebuttondown
    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100 and stamp == "circle" and stamp_state == True:
        surface.blit(circle_button_1, mouse_pos)
        draw = False
        save_flag = False
    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100 and stamp == "square" and stamp_state == True:
        surface.blit(circle_button_2, mouse_pos)
        draw = False
        save_flag = False
    
    # collision detection for COLOR
    if draw == True:    
        if green_rect.collidepoint(mouse_pos):
            brush_color = GREEN
            stamp_state = False
        if red_rect.collidepoint(mouse_pos):
            brush_color = RED
            stamp_state = False
        if blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE
            stamp_state = False
        if pink_rect.collidepoint(mouse_pos):
            brush_color = PINK
            stamp_state = False
        if light_blue_rect.collidepoint(mouse_pos):
            brush_color = LIGHT_BLUE
            stamp_state = False
        if yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW
            stamp_state = False
        if orange_rect.collidepoint(mouse_pos):
            brush_color = ORANGE
            stamp_state = False
        if purple_rect.collidepoint(mouse_pos):
            brush_color = PURPLE
            stamp_state = False
        if dark_green_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN
            stamp_state = False
        if white_rect.collidepoint(mouse_pos):
            brush_color = WHITE
            stamp_state = False
        if brown_rect.collidepoint(mouse_pos):
            brush_color = BROWN
            stamp_state = False
        if pretty_blue_rect.collidepoint(mouse_pos):
            brush_color = PRETTY_BLUE
            stamp_state = False
    #collision detection for eraser
    if draw == True:
        if eraser_rect.collidepoint(mouse_pos):
            brush_color = BLACK
            stamp_state = False
    ## collision detection for CLEAR
    if draw == True:
        if clear_rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, BLACK, screen_rect)
            
    pygame.draw.rect(surface, GRAY, menu_rect)
    surface.blit(menu_text, (10, 20))
    
    pygame.draw.line(surface, BLACK, (0, 40), (100, 40))
    pygame.draw.line(surface, BLACK, (0, 45), (100, 45))
    
    pygame.draw.rect(surface, DARK_GRAY, clear_rect)
    surface.blit(clear_text, (10, 290))

    ##
    surface.blit(brush_text, (10, 160))
    pygame.draw.line(surface, BLACK, (0, 180), (100, 180))
    
    ## draw tutorial 
    surface.blit(tutorial_rec, (400, 20))
    surface.blit(tutorial_tri, (400, 30))
    surface.blit(tutorial_rtri, (400, 40))
    surface.blit(tutorial_rho, (400, 50))
    ## Blit the save rect
    pygame.draw.rect(surface, DARK_GRAY, save_rect)
    surface.blit(save_text, (13, 262))




## Collision detection for SAVE
    
    if draw == True and save_flag == False:
        if save_rect.collidepoint(mouse_pos):
            print("File has been saved.")
            save_surface = pygame.Surface((380, 320))
            save_surface.blit(surface, (0, 0), (100, 0, 380, 320))
            
            
            try:
                with open("saved_files/PaintImage_" + str(file_number) + ".png"):
                    print("file already exists")
                    file_number = file_number + 1
                    save_flag = True
            except IOError:
                save_flag = True
                
            pygame.image.save(save_surface, "saved_files/PaintImage_" + str(file_number) + ".png")
        




 # collision detectin for BRUSH SIZE
    if draw == True:
        if thin_brush.collidepoint(mouse_pos):
            brush_size = 1
        if medium_brush.collidepoint(mouse_pos):
            brush_size = 3
        if thick_brush.collidepoint(mouse_pos):
            brush_size = 5
        if supa_brush.collidepoint(mouse_pos):
            brush_size = 10


# collision detection for STAMP
    if draw == True:
        if circle_rect.collidepoint(mouse_pos):
            stamp = "circle"
            stamp_state = True
        if square_rect.collidepoint(mouse_pos):
            stamp = "square"
            stamp_state = True
            
    
    
    # rect for brush_color
    pygame.draw.rect(surface, GREEN, green_rect)
    if brush_color == GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, green_rect, border)
    
    
    pygame.draw.rect(surface, RED, red_rect)
    if brush_color == RED:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, red_rect, border)
    
    pygame.draw.rect(surface, BLUE, blue_rect)
    if brush_color == BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, blue_rect, border)

    pygame.draw.rect(surface, LIGHT_BLUE, light_blue_rect)
    if brush_color == LIGHT_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, light_blue_rect, border)

    pygame.draw.rect(surface, YELLOW, yellow_rect)
    if brush_color == YELLOW:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, yellow_rect, border)

    pygame.draw.rect(surface, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, orange_rect, border)
    
    pygame.draw.rect(surface, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, orange_rect, border)
    
    pygame.draw.rect(surface, DARK_GREEN, dark_green_rect)
    if brush_color == DARK_GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, dark_green_rect, border)
    
    pygame.draw.rect(surface, PURPLE, purple_rect)
    if brush_color == PURPLE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, purple_rect, border)
    
    pygame.draw.rect(surface, WHITE, white_rect)
    if brush_color == WHITE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, white_rect, border)
    
    pygame.draw.rect(surface, BROWN, brown_rect)
    if brush_color == BROWN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, brown_rect, border)
    
    pygame.draw.rect(surface, PRETTY_BLUE, pretty_blue_rect)
    if brush_color == PRETTY_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, pretty_blue_rect, border)
    
    
    
    # RECT FOR ERASER
    surface.blit(eraser, eraser_rect)
    if brush_color == BLACK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(surface, BLACK, eraser_rect, border)
 



    # Rect for brush size

    
    if brush_size == 1:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(surface, BLACK, thin_brush, brush_border)
    pygame.draw.circle(surface, BLACK, thin_brush.center, 1)
    pygame.draw.rect(surface, BLACK, thin_brush, brush_border)
    
    
    if brush_size == 3:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(surface, BLACK, medium_brush, brush_border)
    pygame.draw.circle(surface, BLACK, medium_brush.center, 3)
    pygame.draw.rect(surface, BLACK, medium_brush, brush_border)
    
    
    if brush_size == 5:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(surface, BLACK, thick_brush, 1)
    pygame.draw.circle(surface, BLACK, thick_brush.center, 5)
    pygame.draw.rect(surface, BLACK, thick_brush, brush_border)
    
    
    if brush_size == 10:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(surface, BLACK, supa_brush, brush_border)
    pygame.draw.circle(surface, BLACK, supa_brush.center, 10)
    pygame.draw.rect(surface, BLACK, supa_brush, brush_border)


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_r]:
        surface.blit(rectangle, mouse_pos)
    if pressed[pygame.K_t]:
        surface.blit(r_triangle, mouse_pos)
    if pressed[pygame.K_y]:
        surface.blit(triangle, mouse_pos)
    if pressed[pygame.K_d]:
        surface.blit(rhombus, mouse_pos)


#s Blitting the stamp
    if stamp == "circle":
        stamp_border = 3
    else:
        stamp_border = 1
    surface.blit(circle_button_1, (5, 120))
    pygame.draw.rect(surface, BLACK, circle_rect, stamp_border)


    if stamp == "square":
        stamp_border = 3
    else:
        stamp_border = 1
    surface.blit(circle_button_2, (47, 120))
    pygame.draw.rect(surface, BLACK, square_rect, stamp_border)
    
    pygame.display.update()
