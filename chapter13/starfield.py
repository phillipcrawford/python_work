import sys

import pygame

from settings import Settings
from star import Star

class Starfield:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Starfield")
        self.stars = pygame.sprite.Group()
        #self.gnu = Gnu(self)

        self._create_stars()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            
            # Redraw the screen during each pass through the loop.
            self._update_screen()

            # 60 frames per second
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()        

    def _create_stars(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens untile there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 3 * star_height):    
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            # Finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += 2 * star_height

    def _create_star(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()
                    
if __name__ == '__main__':
    # Make a game instance and run the game.
    sf = Starfield()
    sf.run_game()