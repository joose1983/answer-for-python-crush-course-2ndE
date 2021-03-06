class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.default_screen_width = 800
        self.default_screen_height = 600
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_limit = 3
        # If fullscreen is True, enter fullscreen mode
        self.fullscreen = False

        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 10        
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        # when game starts, read the high_score from this file;
        # when game about to exit, save the high_score to this file.
        self.high_score_filename = 'high_score.txt'

    def initialize_dynamic_settings(self):
        """Iniialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        
        

        

    

        
