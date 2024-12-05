from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
import sqlalchemy as sa
from sqlalchemy import create_engine
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired
from dotenv import load_dotenv
import os

load_dotenv(".env")

class AddForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired(), InputRequired()])
    author = StringField('Book Author', validators=[DataRequired(), InputRequired()])
    rating = StringField('Rating', validators=[DataRequired(), InputRequired()])
    submit = SubmitField('Add Book')

class UpdateForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired(), InputRequired()])
    author = StringField('Book Author', validators=[DataRequired(), InputRequired()])
    rating = StringField('Rating', validators=[DataRequired(), InputRequired()])
    submit = SubmitField('Update Book')
    

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

bootstrap = Bootstrap5(app)

all_books = []

database_uri = "sqlite:///books-collection.db"

app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db.init_app(app)

# engine = create_engine(database_uri, echo=True)

class Books(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True    )
    name: Mapped[str] = mapped_column(sa.String(255), unique=True)
    author: Mapped[str] = mapped_column(sa.String(255), nullable=False)
    rating: Mapped[float] = mapped_column(sa.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.name}>'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Books).order_by(Books.id)).scalars()
    return render_template('index.html', data = all_books)


@app.route("/add", methods=['GET', 'POST'])
def add_books():
    form = AddForm()
    if form.validate_on_submit():
        title = form.name.data
        author = form.author.data
        rating = form.rating.data

        book = Books(name=title, author=author, rating=rating)

        db.session.add(book)
        db.session.commit()       

        return redirect(url_for('home'))

    return render_template('add.html', form = form)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_books(id):
    form = UpdateForm()
    book = Books.query.get_or_404(id)

    if form.validate_on_submit():
        book.name = form.name.data
        book.author = form.author.data
        book.rating = form.rating.data

        db.session.commit()       

        return redirect(url_for('home'))

    form.name.data = book.name
    form.author.data = book.author
    form.rating.data = book.rating

    return render_template("update.html", form = form)

@app.route("/delete/<int:id>", methods = ["POST"])
def delete_books(id):
    book = Books.query.get_or_404(id)
    db.session.execute(db.delete(Books).where(Books.id == id))
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

