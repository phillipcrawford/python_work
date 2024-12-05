import pygame

class Rocket:
    """A class to manage the player's ship."""

    def __init__(self, rm_game):
        """Initialize the ship and set its starting position"""
        self.screen = rm_game.screen
        self.screen_rect = rm_game.screen.get_rect()
        self.settings = rm_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)