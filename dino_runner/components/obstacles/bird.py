from operator import index
import random as rd

from dino_runner.components.obstacles.obstacles import Obstacle

RECT_BIRD_Y = 250
step_index_bird = 0
class Bird(Obstacle):
    def __init__(self, image, pos_y):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = pos_y
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1


