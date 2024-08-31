from .data_manager_interface import DataManagerInterface
from models import db, User, Movie
from sqlalchemy.exc import SQLAlchemyError

class SQLiteDataManager(DataManagerInterface):
    def __init__(self, app):
        self.db = db

    def get_all_users(self):
        try:
            return User.query.all()
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            return []

    def get_user_movies(self, user_id):
        try:
            return Movie.query.filter_by(user_id=user_id).all()
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            return []

    def get_user_by_id(self, user_id):
        try:
            return User.query.get(user_id)
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            return None

    def get_movie_by_id(self, movie_id):
        try:
            return Movie.query.get(movie_id)
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            return None

    def add_user(self, user):
        try:
            self.db.session.add(user)
            self.db.session.commit()
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            self.db.session.rollback()

    def add_movie(self, movie):
        try:
            self.db.session.add(movie)
            self.db.session.commit()
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            self.db.session.rollback()

    def update_movie(self, movie):
        try:
            self.db.session.commit()
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            self.db.session.rollback()

    def delete_movie(self, movie_id):
        try:
            movie = Movie.query.get(movie_id)
            self.db.session.delete(movie)
            self.db.session.commit()
        except SQLAlchemyError as e:
            print(f"Database error: {str(e)}")
            self.db.session.rollback()