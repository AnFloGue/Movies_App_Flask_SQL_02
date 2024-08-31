from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
import logging
import os
from datamanager.sqlite_data_manager import SQLiteDataManager
from models import db, User, Movie

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance/moviwebapp.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
data_manager = SQLiteDataManager(app)

logging.basicConfig(level=logging.DEBUG)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users')
def list_users():
    users = data_manager.get_all_users()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>')
def user_movies(user_id):
    user = data_manager.get_user_by_id(user_id)
    if not user:
        logging.error(f"User not found: {user_id}")
        return "User not found", 404
    movies = data_manager.get_user_movies(user_id)
    return render_template('movies.html', movies=movies, user_id=user_id)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('username')
        logging.debug(f"Received name: {name}")
        if not name:
            logging.error("Name is required")
            return "Name is required", 400
        user = User(name=name)
        try:
            db.session.add(user)
            db.session.commit()
            logging.debug("User added successfully")
            return redirect(url_for('list_users'))
        except Exception as e:
            logging.error(f"Error adding user: {e}")
            return "Internal server error", 500
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