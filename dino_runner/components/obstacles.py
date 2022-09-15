from dino_runner.utils.constants import SCREEN_WIDTH, SPEED
from dino_runner.utils.constants import obstacles

class Obstacle:
    def __init__(self, image, type:int):
        self.image = image
        self.image_type = type
        self.obst_rect = self.image[self.type].get_rect()
        self.obst_rect_x = SCREEN_WIDTH

    def update(self):
        self.obst_rect_x -= SPEED
        if self.obst_rect_x < -self.obst_rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.image_type], self.obst_rect)