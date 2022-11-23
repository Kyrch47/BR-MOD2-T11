import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH


class Bird(Obstacle):
    def __init__(self):
        self.image = BIRD[0]
        self.flap_index = 0
        super().__init__(BIRD[0])
        self.rect.y = random.randint(200, 300)

    def draw(self, screen):
        if self.flap_index >= 10:
            self.flap_index = 0

        self.image = BIRD[0] if self.flap_index < 5 else BIRD[1]
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.flap_index += 1
