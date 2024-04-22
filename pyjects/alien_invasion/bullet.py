from typing import Any
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manages bullets fired from the ship"""
    
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet and set the position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store position
        self.y = float(self.rect.y)


    def update(self) -> None:
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        """Render the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        