import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, rain_driver):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = rain_driver.screen
        self.settings = rain_driver.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/drop.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the drop to the bottom."""
        self.y += self.settings.drop_speed
        self.rect.y = self.y

    def check_edges(self):
        """Return True if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom)