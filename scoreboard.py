from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 1
        self.hideturtle()

        self.goto(-200,250)
        self.write(f"Level {self.score}",align='center',font=FONT)

        self.update_score()
    def update_score(self):
        self.goto(-200,250)
        self.write(f"Level {self.score}",align='center',font=FONT)
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align = 'center', font=FONT)
