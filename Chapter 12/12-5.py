import sys
import pygame

class TestKeys:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        #self.screen_rect = self.screen.get_rect()
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("TestKeys")
        key_flag = False


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Resopond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                

        

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = TestKeys()
    ai.run_game()
