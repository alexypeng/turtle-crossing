# The car class manages all the functions of the cars in the game.

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 10
STARTING_X = 310


class CarManager:
    def __init__(self):
        """Initialize the car manager."""
        self.cars = []  # Car list that keeps track of all the cars
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates a new car and adds it to the car list."""
        random_chance = random.randint(1, 24)
        if random_chance == 1:  # Ensures that there is not too many cars created
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(STARTING_X, random.randint(-11, 11) * 20 + 15)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.speed = self.speed
            self.cars.append(new_car)

    def move(self):
        """Moves all the cars along the screen."""
        for car in self.cars:
            new_x = car.xcor() - car.speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        """Increases the speed of the cars"""
        self.speed += 0.25

    def delete_car(self, car):
        """Deletes the car inputted from the car list and deletes it as an object."""
        del self.cars[self.cars.index(car)]
