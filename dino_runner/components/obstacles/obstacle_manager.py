import pygame as pg
import random as rd

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if rd.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS, 325))
            
            elif rd.randint(0, 2) == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print('Collisiono xD murio que triste')
                pg.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)