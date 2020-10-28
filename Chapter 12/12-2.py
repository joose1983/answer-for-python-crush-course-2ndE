import sys
import pygame

class Doraemon:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Doraemon")
        #set the backgound color as sky blue
        self.bg_color = (135, 206, 235)

        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('doraemon.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def run_game(self):

        while True:
            self._check_events()
            self.screen.fill(self.bg_color)
            self.blitme()
            pygame.display.flip()
            

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)



if __name__ == '__main__':
    bs = Doraemon()
    bs.run_game()
