import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class DrawStar:

    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (255, 255, 255)
        pygame.display.set_caption("Stars")


        self.stars = pygame.sprite.Group()
        self.star_spacing = 1.5
        self._create_stars()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
        


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _create_stars(self):
        star = Star(self)
        star_width = star.rect.width
        available_space_x = self.screen_width - (self.star_spacing*star_width)
        number_star_x = int(available_space_x // (self.star_spacing*star_width))
        
        star_height = star.rect.height
        available_space_y = (self.screen_height - (self.star_spacing*star_height) - star_height)
        number_rows = int(available_space_y // (self.star_spacing*star_height))
        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                star = Star(self)
                random_number = randint(-10, 10)
                star.x = star_width + random_number*star_width

                #star.x = star_width + 1.5*star_width*star_number
                star.rect.x = int(star.x)
                star.y = star_height + random_number*star_height
                #star.y = star_height + 1.5*star_height*row_number + random_number
                star.rect.y = int(star.y)
            
                self.stars.add(star)
        

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()
        
        
class Star(Sprite):
    def __init__(self, s_game):
        super().__init__()
        self.screen = s_game.screen
        self.image = pygame.image.load('./star.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


        

if __name__ == '__main__':
    #Make a game instance, and run the game.
    s = DrawStar()
    s.run_game()
