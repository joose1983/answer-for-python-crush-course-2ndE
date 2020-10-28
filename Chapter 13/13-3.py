import sys
import pygame
from pygame.sprite import Sprite


class DrawDrops:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (255, 255, 255)
        pygame.display.set_caption("Raining")

        self.drops = pygame.sprite.Group()
        self.drop_spacing = 1.5
        self.dropping_speed = 2
        self._create_drops()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def _create_drops(self):
        drop = Drop(self)
        drop_width = drop.rect.width
        available_space_x = self.screen_width - (self.drop_spacing*drop_width)
        number_drop_x = int(available_space_x // (self.drop_spacing*drop_width))


        for drop_number in range(number_drop_x):
            drop = Drop(self)
            drop.x = drop_width + self.drop_spacing*drop_width*drop_number
            drop.rect.x = int(drop.x)
            self.drops.add(drop)

    def _update_drops(self):
        self.drops.update()
        for drop in self.drops.copy():
            if drop.rect.top > self.screen.get_rect().height:
                self.drops.remove(drop)
            #print(len(self.drops))
        """ when the drops disappeared, create new drops."""
#        if len(self.drops) < 30:
#            self._create_drops()

        
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.drops.draw(self.screen)

        self._update_drops()
        
        pygame.display.flip()


            

class Drop(Sprite):
    def __init__(self, d_game):
        super().__init__()
        self.screen = d_game.screen
        self.image = pygame.image.load('./drop.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.dropping_speed = d_game.dropping_speed

    def update(self):
        self.y += self.dropping_speed
        self.rect.y = int(self.y)
        


if __name__ == '__main__':
    #Make a game instance, and run the game.
    d = DrawDrops()
    d.run_game()
    
    
    
