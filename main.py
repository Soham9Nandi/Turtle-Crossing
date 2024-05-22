import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard






screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tortoise = Player()
level = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(tortoise.move_up,"Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    
    cars.create_cars()
    cars.move_cars()
    
    #Win level, increase score and difficulty
    
    if tortoise.ycor()>=280:
        tortoise.restart()
        level.increase_score()
        cars.update_speed()

    #detect collision with car
    for car in cars.all_cars:
        if car.distance(tortoise)<20:
            level.game_over()
            game_is_on = False

screen.exitonclick()
