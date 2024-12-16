from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, InputRequired
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

class AddPost(FlaskForm):
    title = StringField("Blog post title", validators=[DataRequired(), InputRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired(), InputRequired()])
    author = StringField("Author", validators=[DataRequired(), InputRequired()])
    img_url = StringField("Background Image URL", validators=[DataRequired(), URL(), InputRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Create New Post")

class EditPost(FlaskForm):
    title = StringField("Blog post title", validators=[DataRequired(), InputRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired(), InputRequired()])
    author = StringField("Author", validators=[DataRequired(), InputRequired()])
    img_url = StringField("Background Image URL", validators=[DataRequired(), URL(), InputRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Edit Post")

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/posts/<int:post_id>', methods=["GET"])
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)

@app.route('/new-post', methods=["GET", "POST"])
def add_post():
    # TODO: add_new_post() to create a new blog post
    heading = "New Post"
    form = AddPost()
    if form.is_submitted():
        blog_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            date = date.today().strftime("%B %d %Y"),
            body = form.body.data,
            author = form.author.data,
            img_url = form.img_url.data
        )
        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form = form, heading = heading)


@app.route('/edit-post/<int:post_id>', methods = ["GET", "POST"])
def edit_post(post_id):
    # TODO: edit_post() to change an existing blog post
    heading = "Edit Post"
    blog = db.get_or_404(BlogPost, post_id)
    form = EditPost()
    if form.is_submitted():
        blog.title = form.title.data
        blog.subtitle = form.subtitle.data
        blog.author = form.author.data
        blog.img_url = form.img_url.data
        blog.body = form.body.data

        db.session.commit()

        return redirect(url_for('show_post', post_id=post_id))

    form.title.data = blog.title
    form.subtitle.data = blog.subtitle
    form.author.data = blog.author
    form.img_url.data = blog.img_url
    form.body.data = blog.body

    return render_template('make-post.html', form = form, heading = heading)

@app.route('/delete/<int:post_id>', methods={"GET", "DELETE"})
def delete_post(post_id):
    # TODO: delete_post() to remove a blog post from the database
    blog = db.get_or_404(BlogPost, post_id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
