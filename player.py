from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
#turtle features
SHAPE = "turtle"
COLOR = "black"
SIZE = 1 #how many times the original size


"""creating the Player class that can create the turtle with functions"""
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(SIZE,SIZE)
        self.setheading(90)
        self.penup()
        self.goto(0,-280)

    def move(self):
        self.forward(20)

