# The player class manages all the player's interactions with the game.

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """Initializes the Player"""
        super().__init__()
        self.up()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.reset_position()

    def move_forward(self):
        """Turns the player upward and moves the player up one step."""
        self.setheading(90)
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_backward(self):
        """Turns the player downward and moves the player down one step."""
        self.setheading(-90)
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        """Resets the player to the starting position."""
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        """Checks if the player is at the finish line."""
        return self.ycor() > FINISH_LINE_Y
