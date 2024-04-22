class Settings:
    """Class controlling all the game settings"""

    def __init__(self):
        self.screen_width = 1250
        self.screen_height = 850
        self.bg_color = (0, 0, 0)
        self.frame_rate = 60

        # Ship
        self.ship_limit = 3
        self.level_up_ship_speed = 2

        # Bullets
        self.bullet_width = 3
        # self.bullet_width = 400
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 5
        self.level_up_bullet_speed = 2

        # Aliens
        self.alien_speed_up = 3.0
        self.fleet_drop_speed = 20
        self.level_up_alien_speed = 3
        self.alien_number_decrease = 1

        self.init_dynamic_settings()

    
    def init_dynamic_settings(self):
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.bullet_speed = 5
        self.ship_speed = 5.5
        self.alien_points = 25


    def speed_up(self):
        self.alien_speed += .5
        self.fleet_direction = 1
        self.bullet_speed += 1
        self.ship_speed += 1
        if self.fleet_drop_speed > 15:
            self.fleet_drop_speed -= 1
        self.alien_points += 5