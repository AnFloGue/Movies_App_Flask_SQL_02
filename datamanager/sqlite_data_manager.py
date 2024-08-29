# sqlite_data_manager.py

from datamanager.data_manager_interface import DataManagerInterface
from models import db, Movie, User  # Import the db instance from models.py

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, app):
        self.db = db  # Use the already initialized db instance from models.py

    def get_all_users(self):
        return User.query.all()

    def get_user_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def add_user(self, user):
        self.db.session.add(user)
        self.db.session.commit()

    def add_movie(self, movie):
        self.db.session.add(movie)
        self.db.session.commit()

    def update_movie(self, movie):
        self.db.session.commit()

    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)
        self.db.session.delete(movie)
        self.db.session.commit()

    def get_movie_by_id(self, movie_id):
        return Movie.query.get(movie_id)
