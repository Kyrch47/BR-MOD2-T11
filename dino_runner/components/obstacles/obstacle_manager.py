import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.type = 0

    def update(self, game):
        self.type = random.randint(0, 1)
        if len(self.obstacles) == 0 and self.type == 0:
            self.obstacles.append(Cactus())
        elif len(self.obstacles) == 0 and self.type == 1:
            self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
