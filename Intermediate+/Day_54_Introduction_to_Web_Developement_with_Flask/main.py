from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><hr /><a href='http://127.0.0.1:5000/bye'>Close</a>"

@app.route("/bye")
def say_bye():
    return "<p>Bye, bye!</p>"

if __name__ == "__main__":
    app.run(debug=True)