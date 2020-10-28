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
        


    def run_game(self):

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
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
        

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
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
        
        
    

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ss = SideShooter()
    ss.run_game()

