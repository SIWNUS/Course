import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=player.move)

loop_count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.075)
    screen.update()

    carmanager.generate()
    carmanager.move()

    for car in carmanager.list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
        
    if player.at_end() == True:
        player.next_level()
        carmanager.speed_up()
        scoreboard.update()

    loop_count += 1

screen.mainloop()
