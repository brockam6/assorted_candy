import sys
import pygame

from time import sleep
from game_stats import GameStats
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Main class to manage game assets"""

    def __init__(self):
        """Initialize the game and resources"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.game_active = False
        self.play_button = Button(self, "Play")

        # Game resources
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")
    

    def run_game(self):
        """Run the main loop for the game"""
        while(True):
            self._check_events()
            if self.game_active:
                # Continuously check if the ship is moving
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            if self.stats.ships_left <= 0:
                self.game_active = False
                pygame.mouse.set_visible = True

            self.clock.tick(self.settings.frame_rate)


    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_alien_decrease(self):
        if self.stats.score < 20000:
            self.settings.alien_number_decrease += 1

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        self._check_alien_decrease()
        while current_y < (self.settings.screen_height - 8 * alien_height):
            while current_x < (self.settings.screen_width - self.settings.alien_number_decrease * alien_width):
                # Plus 32 to keep the rendering below the scores
                self._create_alien(current_x, current_y + 32)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, x_pos, y_pos):
        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos
        self.aliens.add(new_alien)
        
        
    def _update_aliens(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            print("WE GOING DOWN")
        self._check_fleet_edges()
        self.aliens.update()
        self._check_aliens_bottom()


    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break


    def _ship_hit(self):
        # Take a life 
        self.stats.ships_left -= 1
        self.sb.prep_ships()

        # Clear the screen
        self.bullets.empty()
        self.aliens.empty()

        # Repopulate
        self._create_fleet()
        self.ship.center_ship()

        # Pause
        sleep(2)


    def _handle_key_release(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False                    
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    

    def _handle_key_press(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True                
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_events(self):
        # Monitor keyboard + mouse input (event loop)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._handle_key_press(event)
            elif event.type == pygame.KEYUP:
                self._handle_key_release(event)


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.init_dynamic_settings()
            pygame.mouse.set_visible(False)
            self.stats.reset_stats()
            self.game_active = True

            # Clear and reset screen
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.sb.prep_ships()


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()
        # Show most recently drawn screen
        pygame.display.flip()


    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _check_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()

    def _check_level_up(self):
        if not self.aliens:
            self.bullets.empty()
            self.settings.speed_up()
            self._create_fleet()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_bullets(self):
        self._check_level_up()
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_collisions()


if __name__ == '__main__':
    """Make game instance and run it"""
    invasion = AlienInvasion()
    invasion.run_game()
