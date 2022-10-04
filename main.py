import pygame
from classes import *
pygame.init()
win=pygame.display.set_mode((1280,600))
pygame.display.set_caption("Pong Pong")
run = True
#colors
white=(255,255,255)
x=10
right=left=False
board=entity()
e=entity()
e_x=pos(0,1)
e_width=e_height=10
e_y=pos(0,20)
gameover=pygame.image.load("gameover.png")
while run:
    if (right and x<=1205):
        x+=5
    if (left and x>=0):
        x-=5
    pygame.time.delay(20)
    e_x.increase()
    e_y.increase()
    if(e_x.val>1280-e_width or e_x.val<0): 
        e_x.flip()
        if (tof() and e_y.val>0):e_y.flip()
        e.colour()
    if(e_y.val<0): 
        e_y.flip()
        if(tof() and (e_x.val<1280-e_width and e_x.val>0)):e_x.flip() 
        e.colour()
    if(e_y.val==580 and e_x.val>=x and e_x.val<=x+75):
        e_y.flip()
        if(tof()):e_x.flip()
        e.colour()
        board.colour()
        print(e.color,board.color)
    if(e_y.val>=600):
        win.blit(gameover, (0,0))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                right=True
            if event.key==pygame.K_a:
                left=True
        if event.type==pygame.KEYUP :
            if event.key==pygame.K_d:
                right=False
            if event.key==pygame.K_a:
                left=False
    win.fill((0,0,0))
    pygame.draw.rect(win,e.color,(e_x.val,e_y.val,e_width,e_height))
    pygame.draw.rect(win, board.color, (x,580,75,15))
    pygame.display.update()