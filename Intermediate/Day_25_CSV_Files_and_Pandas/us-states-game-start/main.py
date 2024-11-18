from turtle import Turtle, Screen
import pandas as pd # type: ignore

# My Solution

# data = pd.read_csv("50_states.csv")

# x = []
# y = []

# for value in data.x:
#     x.append(int(value))

# for value in data.y:
#     y.append(int(value))

# location = []
# for i in range(len(data)):
#     coords = (x[i], y[i])
#     location.append(coords)

# states = data.state.to_list()

# marker = Turtle()
# marker.penup()
# marker.hideturtle()

# screen = Screen()
# screen.screensize(canvwidth=725, canvheight=491)
# screen.title("U.S States Game")
# screen.bgpic("blank_states_img.gif")

# score = 0
# game_on = True

# while game_on:
#     guess = screen.textinput(f"{score}/50 states correct", "Enter your guess:").title()

#     if guess in states:
#         i = states.index(guess)
#         print(f"{guess}, {location[i]}")
#         marker.goto(location[i])
#         marker.write(guess)
#         states.remove(guess)
#         score += 1

#     elif guess.lower() == "exit" or len(states) == 0:
#         game_on = False
#         df = pd.DataFrame(states)
#         df.to_csv("States_to_learn.csv")



# teacher solution

data = pd.read_csv("50_states.csv")

all_states = data.state.to_list()

screen = Screen()
screen.title("U.S States Game")
screen.bgpic("blank_states_img.gif")
guessed_answer = []

while len(guessed_answer) < 50:
    guess = screen.textinput(f"{len(guessed_answer)}/50 states correct", "Enter your guess:").title()

    if guess in all_states:
        guessed_answer.append(guess)
        marker = Turtle()
        marker.penup()
        marker.hideturtle()
        state_data = data[data.state == guess]
        marker.goto(state_data.x.item(), state_data.y.item())
        marker.write(guess)

    elif guess.lower() == "exit":
        # for state in all_states:
        #     if state in guessed_answer:
        #         all_states.remove(state)
        all_states_to_learn = [state for state in all_states if state not in guessed_answer]

        df = pd.DataFrame(all_states_to_learn)
        df.to_csv("States_to_learn.csv")
        break