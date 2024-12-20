from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from argon2 import PasswordHasher
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'secret-key-goes-here'
ph = PasswordHasher(
    time_cost=8,
    parallelism=4,
)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_password = request.form.get('password')
        hashed_password = ph.hash(user_password)
        
        # Check if email already exists
        existing_user = User.query.filter_by(email=request.form.get('email')).first()
        if existing_user:
            flash("Email already registered", "error")
            return redirect(url_for('register'))

        new_user = User(
            name=request.form.get('name'),
            email=request.form.get('email'),
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = None
    if request.method == 'POST':
        mail = request.form.get('email')
        password = request.form.get('password')
        user = db.session.execute(db.select(User).where(User.email == mail)).scalar()

        if user:
            try:
                if ph.verify(user.password, password):
                    login_user(user)
                    return redirect(url_for('home'))
                else:
                    msg = "Invalid login credentials"
                    flash(message=msg, category='error')
                    return redirect(url_for('login'))
            except Exception as e:
                msg = f"Error during login: {str(e)}"
                flash(message=msg, category='error')
                return redirect(url_for('login'))
        else:
            msg = "User doesn't exixt"
            flash(message=msg, category='error')
            return redirect(url_for('login'))
        
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/download')
@login_required
def download():
    try:
        return send_from_directory('static', path='files/cheat_sheet.pdf', as_attachment=True)
    except FileNotFoundError:
        flash("File not found", "error")
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
