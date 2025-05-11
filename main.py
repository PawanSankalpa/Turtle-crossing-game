"""importing modules"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""Editor's panel"""
BACKGROUND_COLOR = "light yellow"

"""setting up the screen"""
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor(BACKGROUND_COLOR)

"""initiating classes"""
turtle = Player()
car_manager = CarManager()
score = Scoreboard()


"""giving commands"""
screen.listen()
screen.onkey(turtle.move , "Up")

game_is_on = True
while game_is_on:
    """screen updating every 0.1 seconds"""
    time.sleep(0.1)
    screen.update()


    """creating new cars and moving them."""
    car_manager.create_car()
    car_manager.move()

    """IF THE TURTLE CROSS THROUGH THE SCREEN THEN ADDS TO THE SCOREBOARD"""
    if turtle.ycor() > 300:
        # adds to the scoreboard and return home
        score.increase_score()
        turtle.goto(0, -280)

    """checking if the turtle hits the car"""
    for car in car_manager.cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            #prints game over and full marks and return
            score.game_over()
            turtle.goto(0, -280)




screen.exitonclick()