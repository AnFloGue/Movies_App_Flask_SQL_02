import unittest
from app import app, db
from models import User, Movie

class MovieWebAppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to MovieWeb App!', response.data)

    def test_add_user(self):
        response = self.app.post('/add_user', data=dict(name='Test User'))
        self.assertEqual(response.status_code, 302)  # Redirect after adding user
        user = User.query.filter_by(name='Test User').first()
        self.assertIsNotNone(user)

    def test_add_movie(self):
        user = User(name='Test User')
        db.session.add(user)
        db.session.commit()
        response = self.app.post(f'/add_movie/{user.id}', data=dict(name='Test Movie', director='Test Director', year=2021, rating=5))
        self.assertEqual(response.status_code, 302)  # Redirect after adding movie
        movie = Movie.query.filter_by(name='Test Movie').first()
        self.assertIsNotNone(movie)

if __name__ == '__main__':
    unittest.main()