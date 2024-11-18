from turtle import Screen
from race import TurtleRace

turtle_list = []
turtle_color = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
emcee = TurtleRace(turtle_list, turtle_color, 6)

emcee.race_arrange()

screen = Screen()
screen.setup(width=550, height=400)

user_bet = screen.textinput(title='BET', prompt='Who will win? Enter a color:').lower()

winner = emcee.turtle_race()

if user_bet == winner:
    print(f"You win the bet! {winner.title()} is the winner.")
else:
    print(f"Sorry, you guessed wrong! {winner.title()} is the winner.")

screen.mainloop()