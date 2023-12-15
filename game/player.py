import pygame

class Player:
    # กำหนดค่าเริ่มต้น
    def __init__(self,pos_x,pos_y,height,width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width

    def get_pos_x(self):
        return self.pos_x
    
    def get_pos_y(self):
        return self.pos_y

    def set_pos_x(self, new_pos_x):
        self.pos_x = new_pos_x
    
    def set_pos_y(self, new_pos_y):
        self.pos_y = new_pos_y

    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width

    def getKeyToMove(self,speed,collision):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and collision[0] == False:
            self.pos_y -= speed
        if keys[pygame.K_s] and collision[1] == False:
            self.pos_y += speed
        if keys[pygame.K_a] and collision[2] == False:
            self.pos_x -= speed
        if keys[pygame.K_d] and collision[3] == False:
            self.pos_x += speed