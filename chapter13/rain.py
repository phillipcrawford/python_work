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
        # self._check_fleet_edges()
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
        new_alien = Drop(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.rain.add(new_alien)

#    def _check_fleet_edges(self):
 #       """Respond appropriately if any aliens have reached an edge."""
  #      for alien in self.aliens.sprites():
   #         if alien.check_edges():
    #            self._change_fleet_direction()
     #           break

#    def _change_fleet_direction(self):
 #       """Drop the entire fleet and change fleet's direction"""
  #      for alien in self.aliens.sprites():
   #         alien.rect.y += self.settings.fleet_drop_speed
    #    self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rain.draw(self.screen)

        pygame.display.flip()
                    
if __name__ == '__main__':
    # Make a game instance and run the game.
    rn = Rain()
    rn.run_game()