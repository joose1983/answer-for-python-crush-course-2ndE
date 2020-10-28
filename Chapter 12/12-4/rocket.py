import sys
import pygame

class Rocket:
    """build a rocket and use direction key to control it"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Rocket")


        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._rocket_update()
            self._update_screen()

    def _check_events(self):
        """Resopond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        if event.key == pygame.K_LEFT:
            self.moving_left = False
        if event.key == pygame.K_UP:
            self.moving_up = False
        if event.key == pygame.K_DOWN:
            self.moving_down = False

    def _rocket_update(self):
        """Update the ship's position based on the movement flag."""
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left >0:
            self.rect.x -= 1
        if self.moving_up and self.rect.top >self.screen_rect.top:
            self.rect.y -= 1
        if self.moving_down and self.rect.down < 0:
            self.rect.y += 1
      
            


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = Rocket()
    ai.run_game()

        

            
