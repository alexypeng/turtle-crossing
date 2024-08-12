# The Scoreboard class manages the scoreboard and game over screens in the game.

from turtle import Turtle

FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        """Initializes the scoreboard."""
        super().__init__()
        self.level = 1
        self.up()
        self.hideturtle()
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard with new information."""
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        """Increases the level displayed by the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Creates the game over screen."""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
