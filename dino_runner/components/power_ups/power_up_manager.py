import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD, SHIELD_TYPE, HAMMER_TYPE, SOUND


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.duration = random.randint(3, 6)
        self.random_index_power_up = random.randint(1, 10)

    def generate_power_up(self, score):        
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)

            if self.random_index_power_up % 2 == 0:
                self.power_ups.append(Shield())

            elif self.random_index_power_up :
                self.power_ups.append(Hammer())

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                if game.player.type ==  HAMMER_TYPE:
                    SOUND[3].play(0, self.duration * 1000)
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)
                elif game.player.type ==  SHIELD_TYPE:
                    SOUND[2].play(0, self.duration * 1000)
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
