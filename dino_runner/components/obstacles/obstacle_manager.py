import pygame as pg
import random as rd

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, GAME_OVER
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if rd.randint(0, 3) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS, 325))

            elif rd.randint(0, 3) == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))

            elif rd.randint(0, 3) == 2:
                self.obstacles.append(Bird(BIRD, 270))

            elif rd.randint(0, 3) == 3:
                self.obstacles.append(Bird(BIRD, 325))

        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print('Se murio ni modos xD')
                pg.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)