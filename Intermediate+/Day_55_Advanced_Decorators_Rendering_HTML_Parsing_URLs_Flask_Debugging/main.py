from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        text = func()
        return f"<b>{text}</b>"
    return wrapper

def make_underlined(func):
    def wrapper():
        text = func()
        return f"<u>{text}</u>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        text = func()
        return f"<em>{text}</em>"
    return wrapper

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><hr /><a href='http://127.0.0.1:5000/bye'>Close</a>"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<p>Bye, bye!</p>"

@app.route("/username")
@app.route("/username/<name>")
@app.route("/username/<int:num>")
@app.route("/username/<name>/<int:num>")
def greet(name=None, num=None):
    if num is None:
        num = 0
    if name is None:
        name = "user"
    return f"Hello there {name}, You are {num} years old!"

if __name__ == "__main__":
    app.run(debug=True)