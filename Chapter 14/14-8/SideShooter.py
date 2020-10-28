import sys
from time import sleep

import pygame
from pygame.sprite import Sprite
from button import Button

class SideShooter:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("SideShooter")
        self.ship = Ship(self)
        self.ship_limit = 2
        self.bullets = pygame.sprite.Group()
        self.screen_rect = self.screen.get_rect()

        self.alien_speed = 1.0
        self.alien_hit_max = 5
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.stats = GameStats(self)

        # Make the Play button.
        self.play_button = Button(self, "Play")
        
    def initialize_settings(self):
        """Iniialize settings that change throughout the game."""
        self.alien_speed = 1.0

    

    def run_game(self):

        while True:
            self._check_events()

            if self.stats.game_active and (self.stats.alien_hit < self.alien_hit_max):
                self.ship.update()
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings.
            self.initialize_settings()
            self._start_game()

    def _start_game(self):
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False) 


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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            self.stats.alien_hit += 1
        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
        
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
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships_left
        self.stats.ships_left -= 1
        if self.stats.ships_left >0:

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

            

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()
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

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)

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
        self.rect.x -= int(self.alien_speed)


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ss_game):
        """Initialize statistics."""
        self.ship_limit = ss_game.ship_limit
        self.alien_hit = 0
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ship_limit
        

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ss = SideShooter()
    ss.run_game()

