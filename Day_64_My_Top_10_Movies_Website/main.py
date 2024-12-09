from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, Text, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired
import requests

class EditForm(FlaskForm):
    rating = FloatField("Your rating: ", validators=[DataRequired(), InputRequired()])
    review = StringField("Your review: ", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Update")

class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("Add Movie")

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mymovies.db'

db.init_app(app)

# CREATE DB
class Movies(db.Model):

    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(235), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(2048), nullable=False)

# CREATE TABLE

with app.app_context():
    db.create_all()
    print("Database tables created.")

# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()
#     print("New movie added to the database.")

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movies).order_by(desc(Movies.rating))).scalars()
    return render_template("index.html", data = movies)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        url = f"http://www.omdbapi.com/?t={title}&apikey=91a21237"
        response = requests.get(url)
        data = response.json()

        if data.get('Response') == 'True':
            title = data.get('Title')
            year = int(data.get('Year', 0))
            description = data.get('Plot', 'No description available')
            rating = float(data.get('imdbRating', 0))
            ranking = int(data.get('Metascore', 0))
            img_url = data.get('Poster', '')

        new_movie = Movies(
            title=title,
            year=year,
            description=description,
            rating=rating,
            ranking=ranking,
            review="",  # Initially no review
            img_url=img_url
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html', form=form)

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    form = EditForm()
    movie = Movies.query.get_or_404(id)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data

        db.session.commit()
        return redirect(url_for('home'))
    
    form.rating.data = movie.rating
    form.review.data = movie.review

    return render_template('edit.html', form = form)

@app.route("/delete/<int:id>", methods=['POST'])
def delete(id):
    movie = Movies.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
