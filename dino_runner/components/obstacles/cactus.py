import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        self.type = random.randint(0, 2)
        self.image = random.choice((SMALL_CACTUS, LARGE_CACTUS))
        if self.image == SMALL_CACTUS:
            self.height = 330
        elif self.image == LARGE_CACTUS:
            self.height = 305
        
        super().__init__(self.image[self.type])
        self.rect.y = self.height
