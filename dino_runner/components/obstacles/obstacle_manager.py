import pygame as pg
import random as rd

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, DINO_SOUND_LOSER
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if rd.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS, 325))

            elif rd.randint(0, 2) == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, 300))

            elif rd.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.death_count += 1
                DINO_SOUND_LOSER.play()
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles = []






