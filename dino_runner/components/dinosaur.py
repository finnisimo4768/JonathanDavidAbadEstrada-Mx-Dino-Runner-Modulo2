import pygame as pg
from pygame.sprite import Sprite

from dino_runner.utils.constants import SOUND, DUCK_IMG, RUN_IMG, JUMP_IMG, DEFAULT_TYPE


DINO_RECT_X = 80
DINO_RECT_Y= 310
JUMP_VEL = 8.5
class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = DINO_RECT_X
        self.dino_rect.y = DINO_RECT_Y
        self.step_index = 0
        self.step_index_duck = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL

        self.has_power_up = False
        self.power_time_up = 0 

    def update(self, user_input):

        if self.dino_run:
            self.run()

        if self.dino_jump:
            self.jump()

        if self.dino_duck:
            self.duck()

        if (user_input[pg.K_UP] and not self.dino_jump) or (user_input[pg.K_SPACE] and not self.dino_jump):
            SOUND[0].play()
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        
        elif user_input[pg.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        
        elif not self.dino_jump:
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = DINO_RECT_X
        self.dino_rect.y = DINO_RECT_Y
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_vel * 4

        self.jump_vel -= 0.8

        if self.jump_vel < -8.5:
            self.dino_rect.y = DINO_RECT_Y
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index_duck//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = DINO_RECT_X
        self.dino_rect.y = DINO_RECT_Y + 30
        self.step_index_duck += 1    

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))