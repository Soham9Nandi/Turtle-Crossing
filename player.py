from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(0,-280)
    def move_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
    def restart(self):
        self.goto(0,-290)