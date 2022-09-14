import pygame as pg
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
SPEED = 20
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pg.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pg.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pg.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pg.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pg.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pg.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pg.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pg.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pg.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pg.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pg.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pg.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pg.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pg.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pg.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pg.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pg.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pg.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAME_OVER = pg.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

DEFAULT_TYPE = "default"
