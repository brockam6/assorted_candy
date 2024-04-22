import pygame
from pygame.sprite import Group, Sprite

class Alien(Sprite):
    """Represents a single alien"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load image, set rect
        self.image = pygame.image.load('images/black_alien.bmp')
        # Every screen object is  tightly bound rectangle. rect represents that object
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Track the aliens exact position (not rounded)
        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
