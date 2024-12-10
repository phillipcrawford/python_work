import sys
import pygame

from settings import Settings
from drop import Drop

class Rain:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rain")
        self.rain = pygame.sprite.Group()
        #self.gnu = Gnu(self)

        self._create_drops()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()  
            self._update_drops()
            self._update_screen()
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

    def _update_drops(self):
        """Update the positions of all aliens in the fleet."""
        self._check_rain_edges()
        self.rain.update()

    def _create_drops(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens untile there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size

        current_x, current_y = drop_width, drop_height
        while current_y < (self.settings.screen_height - drop_height):    
            while current_x < (self.settings.screen_width - 2 * drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width

            # Finished a row; reset x value, and increment y value.
            current_x = drop_width
            current_y += 2 * drop_height

    def _create_drop(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_drop = Drop(self)
        new_drop.y = y_position
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        self.rain.add(new_drop)

    def _check_rain_edges(self):
        """Respond appropriately if any drops have reached an edge."""
        for drop in self.rain.sprites().copy():
            if drop.rect.bottom >= self.screen.get_rect().height:
                self._make_new_drop_row()
                self.rain.remove(drop) 

    def _make_new_drop_row(self):
        """Drop the entire fleet and change fleet's direction"""
        #for drop in self.rain.sprites():

        drop = Drop(self)
        drop_width, drop_height = drop.rect.size

        current_x, current_y = drop_width, drop_height
        while current_x < (self.settings.screen_width - 2 * drop_width):
            self._create_drop(current_x, current_y)
            current_x += 2 * drop_width

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rain.draw(self.screen)

        pygame.display.flip()
                    
if __name__ == '__main__':
    # Make a game instance and run the game.
    rn = Rain()
    rn.run_game()