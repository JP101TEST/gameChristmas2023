#python -m venv myvenv ใช้เพื่อสร้างสภาพแวดล้อมการทำงานเอง
#myvenv\Scripts\activate ใช้เพื่อต้องการใช้งานสภาพแวดล้อมนั้น
#pip install pyinstaller ใช้สร้าง .exe file

import pygame
import sys
import random
from player import Player
from tilemap import Tilemap

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 30) 

color = [(175, 38, 85,255),(163, 183, 99,255),(82, 120, 83,255)]
player_1 = Player(0,720-(16*2),16*2,16*2)
player_1_top_collision = False
player_1_left_collision = False
player_1_right_collision = False
player_1_bottom_collision = False

speed = 1.5
player_1_color = (255,255,255,255)

menu = True

selected = 0

# Set up the text and its position
text = ""
textCollision = "Collision:False"

tile = (1, 2)
print(tile," [1]=",tile[0]," [2]=",tile[1])

tilemap = []


for i in range(18):#36 to 18
    row = []
    for j in range(36):
        t = Tilemap(((32*2)+(32*i),(32*2)+(32*j)),(32,32),random.randint(0,2))
        row.append(t)
    tilemap.append(row)

# for i in range(18):#36 to 18
#     print(len(tilemap),"|",len(tilemap[0]),"|",tilemap[i][35].get_pos_x(),"|",tilemap[i][35].get_pos_y())

for i in range(0,18):
        for j in range(0,36):
            print(tilemap[i][j].get_pos_x(),"|",tilemap[i][j].get_pos_y())
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player_1_react = pygame.Rect(player_1.get_pos_x(), player_1.get_pos_y(), player_1.get_height(), player_1.get_width())
    player_1_react_top = pygame.Rect(player_1.get_pos_x()+2, player_1.get_pos_y()-1, player_1.get_width()-4, 2)
    player_1_react_left = pygame.Rect(player_1.get_pos_x()-2, player_1.get_pos_y()+4, 2, player_1.get_height()-8)
    player_1_react_right = pygame.Rect(player_1.get_pos_x()+32, player_1.get_pos_y()+4, 2, player_1.get_height()-8)
    player_1_react_bottom = pygame.Rect(player_1.get_pos_x()+2, player_1.get_pos_y()+32, player_1.get_width()-4, 2)
    
    for i in range(0,18):
        for j in range(0,36):
            if player_1_react.colliderect(pygame.Rect(tilemap[i][j].get_PS())):
                textCollision = "Collision:True"
            if player_1_react.colliderect(pygame.Rect(tilemap[i][j].get_PS())) and tilemap[i][j].get_type() == 2:
                speed =3.5
            if player_1_react_top.colliderect(pygame.Rect(tilemap[i][j].get_PS())) and tilemap[i][j].get_type() == 0:
                player_1_top_collision = True
            if player_1_react_left.colliderect(pygame.Rect(tilemap[i][j].get_PS())) and tilemap[i][j].get_type() == 0:
                player_1_left_collision = True
            if player_1_react_right.colliderect(pygame.Rect(tilemap[i][j].get_PS())) and tilemap[i][j].get_type() == 0:
                player_1_right_collision = True
            if player_1_react_bottom.colliderect(pygame.Rect(tilemap[i][j].get_PS())) and tilemap[i][j].get_type() == 0:
                player_1_bottom_collision = True

    if menu == True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            speed += 0.5
        if keys[pygame.K_LEFT]:
            if speed - 0.5 >0:
                speed -= 0.5
        player_1.getKeyToMove(speed,(player_1_top_collision,player_1_bottom_collision,player_1_left_collision,player_1_right_collision))

    mouse = pygame.mouse.get_pos()

    text = ["speed = " + str(speed) ,"player_pos = ["+str(player_1.get_pos_x())+","+str(player_1.get_pos_y())+"]","mouse_pos = ["+str(mouse[0])+","+str(mouse[1])+"]"]
    
    textPlayer_1_top_collision = "p c t:"+str(player_1_top_collision)
    textPlayer_1_left_collision = "p c l:"+str(player_1_left_collision)
    textPlayer_1_right_collision = "p c r:"+str(player_1_right_collision)
    textPlayer_1_bottom_collision = "p c b:"+str(player_1_bottom_collision)
    
    textPlayer_1_top_collision = "p c t:"+str(player_1_top_collision)
    textPlayer_1_left_collision = "p c l:"+str(player_1_left_collision)
    textPlayer_1_right_collision = "p c r:"+str(player_1_right_collision)
    textPlayer_1_bottom_collision = "p c b:"+str(player_1_bottom_collision)

    text_render_1 = font.render(text[0], True, (255, 255, 150,255))
    text_render_2 = font.render(text[1], True, (255, 255, 150,255))
    text_render_3 = font.render(text[2], True, (255, 255, 150,255))
    text_render_4 = font.render(textCollision, True, (255, 255, 150,255))
    text_render_5 = font.render(textPlayer_1_top_collision, True, (255, 255, 150,255))
    text_render_6 = font.render(textPlayer_1_left_collision, True, (255, 255, 150,255))
    text_render_7 = font.render(textPlayer_1_right_collision, True, (255, 255, 150,255))
    text_render_8 = font.render(textPlayer_1_bottom_collision, True, (255, 255, 150,255))
    #clear drawing    
    screen.fill("black")

    for i in range(0,18):
        for j in range(0,36):
            pygame.draw.rect(screen,color[tilemap[i][j].get_type()],pygame.Rect(tilemap[i][j].get_pos_y(),tilemap[i][j].get_pos_x() , tilemap[i][j].get_height(), tilemap[i][j].get_width()))

    pygame.draw.rect(screen,(255, 255, 255, 255),player_1_react)

    pygame.draw.rect(screen,(115, 225, 15, 255),player_1_react_top)
    pygame.draw.rect(screen,(115, 225, 15, 255),player_1_react_left)
    pygame.draw.rect(screen,(115, 225, 15, 255),player_1_react_right)
    pygame.draw.rect(screen,(115, 225, 15, 255),player_1_react_bottom)

    screen.blit(text_render_1, (0,0))
    screen.blit(text_render_2,  (120,0))
    screen.blit(text_render_3,  (420,0))
    screen.blit(text_render_4,  (0,30))
    screen.blit(text_render_5,  (0,60))
    screen.blit(text_render_8,  (0,120))
    screen.blit(text_render_6,  (0,80))
    screen.blit(text_render_7,  (0,100))
    

    #drawing  
    pygame.display.flip()

    textCollision = "Collision:False"
    player_1_top_collision = False
    player_1_left_collision = False
    player_1_right_collision = False
    player_1_bottom_collision = False
    speed = 1.5
    

    clock.tick(60)

pygame.quit()