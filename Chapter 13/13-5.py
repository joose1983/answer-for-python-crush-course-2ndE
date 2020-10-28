import sys
import pygame
from pygame.sprite import Sprite

class SideShooter:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("SideShooter")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.screen_rect = self.screen.get_rect()

        self.alien_speed = 1
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            


    def _check_events(self):
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
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True            

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
        #print(len(self.bullets))
        
    def _create_fleet(self):
        """ Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_width = self.ship.rect.width
        available_space_x = (self.screen_width - (3* alien_width) - ship_width)
        number_aliens_x = available_space_x // (2*alien_width)
        
        # Determin the number of rows of aliens that fit on the screen.
        available_space_y = self.screen_height - (2 * alien_height)
        number_aliens_y = available_space_y // (2*alien_width)
        
        # Create the full fleet of aliens.
        for column_number in range(number_aliens_x):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number,column_number)
        

    def _create_alien(self, alien_number, column_number):
        # Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.rect.x = self.screen_width - alien_width - 2*alien_width*column_number
        alien.rect.y = alien.rect.height + 2*alien.rect.height*alien_number


        self.aliens.add(alien)
        
    def _update_aliens(self):
        """update the positions of all aliens in the fleet."""

        self.aliens.update()



    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        pygame.display.flip()


class Ship:
    def __init__(self, ss_game):
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()

        self.image = pygame.image.load('./ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        #Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.color = (60, 60, 60)
        self.bullet_width = 15
        self.bullet_height = 3
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midleft = ss_game.ship.rect.midright
        self.bullet_speed = 1

    def update(self):
        self.rect.x += self.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen

        # Load the alen image and set its rect attribute.
        self.image = pygame.image.load('./alien.bmp')
        self.rect =self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = ss_game.screen_width - self.rect.width
        self.rect.y = self.rect.height
        

        self.alien_speed = ss_game.alien_speed


        

    def update(self):
        """Move the alien right or left."""
        #self.x -= self.alien_speed
        #self.rect.x = int(self.x)
        self.rect.x -= self.alien_speed
        

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ss = SideShooter()
    ss.run_game()

