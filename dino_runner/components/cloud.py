import random as rdm
from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD

speed_cloud = 17

class Cloud:
    def __init__(self):
        self.image = CLOUD
        self.width = self.image.get_width()
        self.cloud_x = SCREEN_WIDTH + rdm.randint(800, 1000)
        self.cloud_y = rdm.randint(50, 100)

    def update(self):
        self.cloud_x -= speed_cloud
        if self.cloud_x < -self.width:
            self.cloud_x = SCREEN_WIDTH + rdm.randint(2500, 3000)
            self.cloud_y = rdm.randint(50, 100)
        self.draw()
    
    def draw(self, screen):
        screen.blit(self.image, (self.cloud_x, self.cloud_y))