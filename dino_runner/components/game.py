import pygame as pg

from dino_runner.utils.constants import BG, HAMMER_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DINO_DEAD, GAME_OVER, FONT_STYLE, DEFAULT_TYPE, COLOURS

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


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
        self.power_up_manager = PowerUpManager()
        self.running = False
        self.score = 0
        self.death_count = 0
        self.hi_score = 0

    def update_score(self):
        self.score += 1

        if self.score % 100 == 0 and self.game_speed < 700:
            self.game_speed += 5

        if self.score > self.hi_score:
            self.hi_score = self.score

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                if self.death_count == 0:
                    self.show_menu()
                else:
                    self.screen_death()

        pg.display.quit()
        pg.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False


    def reset_game(self):
        self.score = 0 
        self.obstacle_manager.reset_obstacle()
        self.playing = True
        self.game_speed = 20
        self.power_up_manager.reset_power_ups()

    def update(self):
        self.update_score()
        user_input = pg.key.get_pressed()

        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.cloud.update(self.game_speed)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.obstacle_manager.draw(self.screen)
        self.cloud.draw(self.screen)
        self.power_up_manager.draw(self.screen)

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

    def gen_text(self, word:str, half_screen_width:int, half_screen_height:int, color:str, size:int):
        font = pg.font.Font(FONT_STYLE, size)

        text = font.render(word, True, COLOURS[color])
        text_rec = text.get_rect()
        text_rec.center = (half_screen_width, half_screen_height)

        self.screen.blit(text, text_rec)

    def draw_score(self):
        if self.death_count == 0:
            self.gen_text(f'Score: {self.score}', 970, 50, 'black', 30)
        else :
            self.gen_text(f'Hi: {self.hi_score}', 100, 50, 'yellow', 30)
            self.gen_text(f'Score: {self.score}', 970, 50, 'black', 30)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pg.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                if self.player.type == HAMMER_TYPE:
                    self.gen_text(f'{self.player.type.capitalize()} enabled for:  {time_to_show}  seconds', 500, 150, 'black', 18)
                else:
                    self.gen_text(f'{self.player.type.capitalize()} enabled for:  {time_to_show}  seconds', 500, 150, 'purple', 18)
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pg.KEYDOWN:
                self.run()

    def show_menu(self):

        self.running = True

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.screen.fill(COLOURS['white'])
        self.gen_text('Press any key to start ..', half_screen_width, half_screen_height, 'black', 50)

        pg.display.update()
        self.handle_events_on_menu()

    def screen_death(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        self.screen.fill(COLOURS['white'])
        self.screen.blit(GAME_OVER, (365, 100))
        self.screen.blit(DINO_DEAD, (500, 190))
        self.gen_text('Press any key to continue ..', half_screen_width, half_screen_height + 200, 'black', 40)
        self.gen_text(f'Score: {self.score}', half_screen_width, half_screen_height + 70, 'green', 30)
        self.gen_text(f'Death Count: {self.death_count}', half_screen_width, half_screen_height + 130, 'red', 30)

        pg.display.update()
        self.handle_events_on_menu()
