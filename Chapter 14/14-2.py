import sys
from time import sleep

import pygame
from pygame.sprite import Sprite
import pygame.font

class TargetPractice:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("TargetPractice")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.screen_rect = self.screen.get_rect()

        self.stats = GameStats(self)
        self.rectangle = pygame.sprite.Group()
        self.rectangle_target = Rectangle(self)
        self.rectangle.add(self.rectangle_target)

        # Make the Play button.
        self.play_button = Button(self, "Play")

        
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_rectangle()            

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
            self._start_game()

    def _start_game(self):
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of any remaining bullets.
        self.bullets.empty()

        # Create a new fleet and center the ship.
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
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.rectangle, True, False)
        
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.stats.fired_bullets += 1
                self.bullets.remove(bullet)    

        if self.stats.fired_bullets >= self.stats.rectangle_miss_max:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
              

    def _update_rectangle(self):

        self.rectangle.update()



    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.rectangle.draw(self.screen)
        # Draw the play button if the game is inactive.
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
        self.bullet_height = 100
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midleft = ss_game.ship.rect.midright
        self.bullet_speed = 1

    def update(self):
        self.rect.x += self.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Rectangle(Sprite):
    """This is the target class"""
    def __init__(self, tp_game):
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = tp_game.screen.get_rect()
        self.image = pygame.image.load('./rectangle.bmp')
        self.rect =self.image.get_rect()

        self.rect.midright = self.screen_rect.midright
        self.rectangle_speed = 2
        # Moving flags
        self.moving_up = True
        
        

    def update(self):
        if self.rect.top < self.screen_rect.top:
            self.moving_up = False
        if self.rect.bottom > self.screen_rect.bottom:
            self.moving_up = True
            
        if self.moving_up:
            self.rect.y -= 1
        if not self.moving_up:
            self.rect.y += 1

class Button:

    def __init__(self, tp_game, msg):
        """Initialize button attributes."""
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill (self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ss_game):
        """Initialize statistics."""

        self.rectangle_miss_max = 1
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False
        self.fired_bullets = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.fired_bullets = 0




        

if __name__ == '__main__':
    #Make a game instance, and run the game.
    tp = TargetPractice()
    tp.run_game()

                
