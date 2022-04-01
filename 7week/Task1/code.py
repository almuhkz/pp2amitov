import pygame as pg
from datetime import datetime

def rotate(surface, angle, pivot, offset):
    rotate_image = pg.transform.rotozoom(surface, -angle, 1)
    rotate_offset = offset.rotate(angle) 
    rect = rotate_image.get_rect(center=pivot+rotate_offset)
    return rotate_image, rect  
def sec_update():
    ntime = datetime.now()
    angle = (int(ntime.second))/12*72
    return angle
def min_update():
    ntime = datetime.now()
    angle = (int(ntime.minute))/12*72
    return angle

pg.init()
screen = pg.display.set_mode((1400, 1050))
background = pg.image.load("backgroun.png")
clock = pg.time.Clock()
left_h = pg.image.load('lefthand.png')
right_h = pg.image.load('righthand.png')
pivot = [700, 520]
offset = pg.math.Vector2(10, -70)
ntime = datetime.now()
angle = (int(ntime.minute))/12*72
pivot_r = [700, 520]
offset_r = pg.math.Vector2(5, -140)
angle_r = (int(ntime.second))/12*72

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    angle=min_update()
    angle_r=sec_update()
    rotated_image, rect = rotate(left_h, angle, pivot, offset)
    rotated_image_r, rect_r = rotate(right_h, angle_r, pivot_r, offset_r)
    screen.blit(background,(0,0))
    screen.blit(rotated_image, rect)
    screen.blit(rotated_image_r, rect_r)  
    pg.display.flip()
    clock.tick(60)
