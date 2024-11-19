from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)

@app.route("/")
def game():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src=' https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' style=width:300px; height:300px; />"

@app.route("/<int:num>")
def check(num):
    if num < random_num:
        return f"<p style=color:red;><b>{num} is too low:</b></p>" \
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' style=width:300px; height:300px; /"
    elif num > random_num:
        return f"<p style=color:purple;><b>{num} is too high:</b></p>" \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' style=width:300px; height:300px; />"
    elif num == random_num:
        return f"<p style=color:green;><b>You found me.</b></p>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' style=width:300px; height:300px; />"

if __name__ == "__main__":
    app.run(debug=True)