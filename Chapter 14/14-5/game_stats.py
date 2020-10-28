class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False

        # Read high score from a file
        self.high_score = 0
        self.high_score_filename = ai_game.settings.high_score_filename
        self.read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        try:
            with open(self.high_score_filename) as file_object:
                lines = file_object.readlines()
                if lines:
                    high_score_str = lines[0]          
                    self.high_score = int(high_score_str)
        except FileNotFoundError:
            # High score should never be reset
            self.high_score = 0
