import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    """A class to represent a missile around the aliens, if it is hit, the bullets get bigger for a moment."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the missile image and set its rect attribute.
        self.image = pygame.image.load('images/missile.png')
        self.rect =self.image.get_rect()

        # Start each new missile near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the missile's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if missile is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        

    def update(self):
        """Move the missile right or left."""
        self.x += self.settings.missile_speed * self.settings.missile_direction
        self.rect.x = self.x
