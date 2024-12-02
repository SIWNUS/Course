from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL, InputRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(), InputRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL(), InputRequired()])
    opening = TimeField('Open Time', validators=[DataRequired(), InputRequired()])
    closing = TimeField('Close Time', validators=[DataRequired(), InputRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'], validate_choice=True, validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=['✘' ,'💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validate_choice=True, validators=[DataRequired()])
    power_rating = SelectField('Power Outlet Charge Rating', choices=['✘' ,'🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validate_choice=True, validators=[DataRequired()])
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        cafe = form.cafe.data
        location = form.location.data
        opening = form.opening.data
        closing = form.closing.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data

        data_to_append = [cafe, location, opening, closing, coffee_rating, wifi_rating, power_rating]

        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as fp:
            writer = csv.writer(fp)
            writer.writerow(data_to_append)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
