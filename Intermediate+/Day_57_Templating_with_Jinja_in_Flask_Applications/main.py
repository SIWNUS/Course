from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts = blog_response.json()
    return render_template("index.html", posts=blog_posts)

@app.route("/post/<int:num>")
def blog(num):
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts = blog_response.json()
    post = blog_posts[num - 1]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
