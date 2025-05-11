"""importing the turtle module,random module"""
from turtle import Turtle
from random import choice,randint

"""Editor's panel"""
COLORS = ["red", "orange", "pink", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

"""creating the class"""
class CarManager:

    """car list #so that we can use it through loops to move them and easily manipulate them"""
    def __init__(self):
        self.cars = []

    """creating car with features to our liking and add them to our cars list"""
    def create_car(self):
        random_number = randint(0, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(320, randint(-250, 250))
            self.cars.append(new_car)

    """move function"""
    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)









