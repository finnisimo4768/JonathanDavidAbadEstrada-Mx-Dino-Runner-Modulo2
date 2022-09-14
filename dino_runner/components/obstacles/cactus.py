import pygame as pg
import random as rd

from dino_runner.components.obstacles.obstacles import Obstacle


class Cactus(Obstacle):
    def __init__(self, image, coor_y):
        self.type = rd.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = coor_y
