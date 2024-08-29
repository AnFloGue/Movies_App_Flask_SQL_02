
from flask import Flask, render_template, request, redirect, url_for
from datamanager.sqlite_data_manager import SQLiteDataManager
from models import db, User, Movie  # Import db from models.py
import os


app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance/moviwebapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object with Flask app
db.init_app(app)

# Initialize the SQLiteDataManager with the existing db instance
data_manager = SQLiteDataManager(app)

@app.route('/')
def home():
    return "Welcome to MovieWeb App!"

@app.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>')
def user_movies(user_id):
    movies = data_manager.get_user_movies(user_id)
    return render_template('movies.html', movies=movies, user_id=user_id)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        user = User(name=name)
        data_manager.add_user(user)
        return redirect(url_for('list_users'))
    return render_template('add_user.html')

@app.route('/users/<int:user_id>/add_movie', methods=['GET', 'POST'])
def add_movie(user_id):
    if request.method == 'POST':
        name = request.form['name']
        director = request.form['director']
        year = request.form['year']
        rating = request.form['rating']
        movie = Movie(name=name, director=director, year=year, rating=rating, user_id=user_id)
        data_manager.add_movie(movie)
        return redirect(url_for('user_movies', user_id=user_id))
    return render_template('add_movie.html', user_id=user_id)

@app.route('/users/<int:user_id>/update_movie/<int:movie_id>', methods=['GET', 'POST'])
def update_movie(user_id, movie_id):
    movie = data_manager.get_movie_by_id(movie_id)
    if request.method == 'POST':
        movie.name = request.form['name']
        movie.director = request.form['director']
        movie.year = request.form['year']
        movie.rating = request.form['rating']
        data_manager.update_movie(movie)
        return redirect(url_for('user_movies', user_id=user_id))
    return render_template('update_movie.html', movie=movie)

@app.route('/users/<int:user_id>/delete_movie/<int:movie_id>')
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(url_for('user_movies', user_id=user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
