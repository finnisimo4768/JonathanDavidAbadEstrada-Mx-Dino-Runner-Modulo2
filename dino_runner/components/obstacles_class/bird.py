import random as rdm
from dino_runner.components.obstacles import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        self.image_type = 0
        super().__init__(image, self.image_type)
        self.rect_y = 250
        self.step_index = 0


    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image_type[0 if self.step_index < 5 else 1], self.obst_rect)
        self.index += 1

