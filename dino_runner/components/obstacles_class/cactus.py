import random as rdm
from dino_runner.components.obstacles import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.image_type = rdm.randint(0,2)
        super().__init__(image, self.image_type)
        self.rect_y = 315

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.image_type = rdm.randint(0,2)
        super().__init__(image, self.image_type)
        self.rect_y = 305