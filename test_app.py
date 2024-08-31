import unittest
from app import app, db
from models import User, Movie

class MovieWebAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client for making requests
        self.app_context = app.app_context()
        self.app_context.push()
        app.config['TESTING'] = True  # Enable testing mode for the app
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/antoniofloresguerrero/PycharmProjects/_MasterSchool/GitHub/To_Github/Movies_App_Flask_SQL_02/instance/moviwebapp.db'
        db.create_all()  # Create all database tables (if they don't exist)

        # Create a user object before accessing its id
        self.user = User(name='Test User')
        db.session.add(self.user)
        db.session.commit()  # Commit changes to the database

    def tearDown(self):
        db.session.remove()  # Remove objects from the session
        db.drop_all()  # Drop all database tables
        self.app_context.pop()  # Pop the app context

    def test_home_page(self):
        response = self.app.get('/')  # Send a GET request to the homepage
        self.assertEqual(response.status_code, 200)  # Check for successful response
        self.assertIn(b'Welcome to MovieWeb App!', response.data)  # Check for content

    def test_add_user(self):
        # Test with an empty name
        response = self.app.post('/add_user', data=dict(name=''))  # POST with empty name
        self.assertEqual(response.status_code, 400)  # Expect 400 for missing name
        self.assertIn(b'Name is required', response.data)  # Check for error message

        # Test with a valid name (using the pre-created user)
        response = self.app.post('/add_user', data=dict(name=self.user.name))  # POST with valid name
        self.assertEqual(response.status_code, 302)  # Redirect after adding user

    def test_add_movie(self):
        # Verify the user was added
        self.assertIsNotNone(User.query.filter_by(name=self.user.name).first())

        # Send a POST request to add a movie for the created user
        response = self.app.post(f'/users/{self.user.id}/add_movie', data=dict(
            name='Test Movie',
            director='Test Director',
            year=2021,
            rating=5
        ))

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Verify the movie was added to the database
        movie = Movie.query.filter_by(name='Test Movie').first()
        self.assertIsNotNone(movie)
        self.assertEqual(movie.director, 'Test Director')
        self.assertEqual(movie.year, 2021)
        self.assertEqual(movie.rating, 5)