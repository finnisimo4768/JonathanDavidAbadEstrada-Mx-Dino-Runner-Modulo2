import pygame as pg

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DINO_DEAD, GAME_OVER

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.display.set_icon(ICON)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.game_speed = 20
        self.playing = False
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.cloud = Cloud()
        self.obstacle_manager = ObstacleManager()
        self.running = False
        self.score = 0
        self.death_count = 0

    def update_score(self):
        self.score += 1

        if self.score % 100 == 0 and self.game_speed < 2000:
            self.game_speed += 5

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.score = 0
                self.death_count = 0
                self.show_menu()
        pg.display.quit()
        pg.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacle()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pg.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update(self.game_speed)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_score()
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        pg.display.update()
        pg.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def gen_text(self, word:str, half_screen_width:int, half_screen_height:int):
        self.screen.fill((255, 255, 255))
        font = pg.font.Font(FONT_STYLE, 30)
        text = font.render(f'{word}', True, (0, 0, 0))
        text_rec = text.get_rect()
        text_rec.center = (half_screen_width, half_screen_height)
        self.screen.blit(text, text_rec)

    def gen_text_score(self, score, word, width, height):
        font = pg.font.Font(FONT_STYLE, 30)
        text = font.render(f'{word}: {str(score)}', True, (0, 0, 0))
        text_rec = text.get_rect()
        text_rec.center = (width, height)
        self.screen.blit(text, text_rec)

    def draw_score(self):
        self.gen_text_score(self.score, 'Score', 1000, 50)

    def handle_events_on_menu(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pg.KEYDOWN:
                self.run()

    def show_menu(self):

        self.running = True

        while self.running:
            if self.death_count == 0:
                half_screen_height = SCREEN_HEIGHT // 2
                half_screen_width = SCREEN_WIDTH // 2
                self.gen_text('Pres any key to start ..', half_screen_width, half_screen_height)

            else:
                save_score = self.score
                half_screen_height = SCREEN_HEIGHT // 2
                half_screen_width = SCREEN_WIDTH // 2

                self.screen.fill((255, 255, 255))
                self.screen.blit(GAME_OVER, (365, 100))
                self.screen.blit(DINO_DEAD, (500, 190))
                self.gen_text_score(save_score, 'Score', half_screen_width, half_screen_height + 50)
                self.gen_text_score(self.death_count, 'Death Count', half_screen_width, half_screen_height + 100)

            pg.display.update()
            self.handle_events_on_menu()
