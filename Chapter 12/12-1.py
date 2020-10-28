import sys
import pygame

class BlueSky:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("BlueSky")
        #set the backgound color as sky blue
        self.bg_color = (135, 206, 235)

    def run_game(self):

        while True:
            self._check_events()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

   



if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()
    
