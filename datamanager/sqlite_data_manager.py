from .data_manager_interface import DataManagerInterface
from models import db, User, Movie

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, app):
        self.db = db

    def get_all_users(self):
        return User.query.all()

    def get_user_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)
    
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