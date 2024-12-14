from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

def str_to_bool(value):
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    return None

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafe = random.choice(cafes)

    return jsonify(rand_cafe=cafe.to_dict())

@app.route("/all", methods=["GET"])
def all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()

    cafes_data = [cafe.to_dict() for cafe in all_cafes]

    return jsonify(cafes_data)

@app.route("/search", methods=["GET"])
def search():
    loc = request.args.get("loc")

    result = db.session.execute(db.select(Cafe).where(Cafe.location==loc))
    all_result_cafe = result.scalars().all()

    result_data = [cafe.to_dict() for cafe in all_result_cafe]

    return jsonify(result_data)

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("has_toilet")),
        has_wifi = bool(request.form.get("has_wifi")),
        has_sockets = bool(request.form.get("has_sockets")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response= {"success": "Successfully added the new cafe!"})

# HTTP PUT/PATCH - Update Record
@app.route("/update-cafe/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):
    new_price = request.args.get("coffee_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify(response = {"success": "Successfully updated price."})
    else:
        return jsonify(response = {"error": {"Not_Found": "A cafe with this id was not found in this database."}})


# HTTP DELETE - Delete Record
@app.route("/record-closed/<int:cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"200": "The request has succeeded."})
        else:
            return jsonify(error={"404": "A 404 error occurs when the origin server did not find a current representation for the target resource, or it is not willing to disclose that one exists."})
    else:
        return jsonify(error={"403": "The server understood the request but refuses to authorize it."})

if __name__ == '__main__':
    app.run(debug=True)
