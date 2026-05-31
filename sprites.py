import pygame
from game_object import GameObject

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 30, (0, 255, 0)) # Green player
        self.speed = 6

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

    def shoot(self):
        # Spawn a laser from the top-center of the player
        return Laser(self.rect.centerx - 2, self.rect.top)


class Alien(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 30, (255, 0, 0)) # Red alien
        self.speed = 2

    def update(self):
        # Aliens just march downward for simplicity
        self.rect.y += self.speed


class Laser(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 5, 15, (255, 255, 0)) # Yellow laser
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed