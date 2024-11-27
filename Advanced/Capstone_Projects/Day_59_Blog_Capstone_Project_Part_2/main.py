from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    blog_response = requests.get(url="https://api.npoint.io/e8e87c01790bd4c09cc2")
    blog_posts = blog_response.json()
    image_url = "https://images.unsplash.com/photo-1732624697703-c5b0d3110cb4?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    return render_template("index.html", posts=blog_posts, image_url = image_url)

@app.route("/post/<int:num>")
def post(num):
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts = blog_response.json()
    post = blog_posts[num - 1]
    urls = ["https://i1.wp.com/blog.plantdelights.com/wp-content/uploads/2015/08/Ferocactus-wislizeni-A3AZ-028-in-flower.jpg", "https://c2.staticflickr.com/4/3026/2838434910_d770a0bb94_z.jpg?zz=1", "https://dinnerthendessert.com/wp-content/uploads/2019/11/Fruit-Cake-Muffins-16x9.jpg"]
    image_url = urls[num - 1]
    return render_template("post.html", post=post, image_url=image_url)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)