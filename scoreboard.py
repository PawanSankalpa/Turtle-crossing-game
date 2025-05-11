"""importing the turtle module"""
from turtle import Turtle

"""Editor's panel"""
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
GAME_OVER_FONT = ("Bold", 44, "normal")

"""creating the scoreboard class"""
class Scoreboard(Turtle):

    """creating where the score should appear"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-270,270)
        self.update_scoreboard()

    """updating the scoreboard with text"""
    def update_scoreboard(self):
        self.write(f"Your Score : {self.score}", align=ALIGNMENT, font=FONT)

    """game over function"""
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over, Scores : {self.score}" , align=ALIGNMENT , font=GAME_OVER_FONT)

    """each time scores 1 will be added and clear the previous screen"""
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()


