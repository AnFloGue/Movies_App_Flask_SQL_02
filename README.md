# MovieWeb App

## Overview

MovieWeb App is a web application that allows users to manage their favorite movies. Users can add, update, and delete movies from their list. The application uses Flask for the web framework and SQLAlchemy for database interactions with SQLite.

## Application Structure

### User Interface (UI)

#### Flask
Handles routing and rendering HTML templates.

#### HTML
Templates provide the necessary forms and links for user interactions.

### Data Management

#### Python Class
`SQLiteDataManager` class in `sqlite_data_manager.py` handles operations related to the data source, such as getting users and their movies, adding, updating, and deleting movies.

#### Database File

##### SQLite
Using an SQLite database (`moviwebapp.db`) to store user and movie data.

## Core Functionalities

### User Selection

#### Route
`/users` route lists all users, allowing for user selection.

### Movie Management

#### Add a Movie
`/users/<int:user_id>/add_movie`

#### Delete a Movie
`/users/<int:user_id>/delete_movie/<int:movie_id>`

#### Update a Movie
`/users/<int:user_id>/update_movie/<int:movie_id>`

#### List All Movies
`/users/<int:user_id>`

### Data Source Management

#### SQLiteDataManager
This class manages interactions with the SQLite database, including CRUD operations for users and movies.

## Endpoints

### Home
- **URL**: `/`
- **Method**: GET
- **Description**: Displays the home page.

### List Users
- **URL**: `/users`
- **Method**: GET
- **Description**: Lists all users.

### User Movies
- **URL**: `/users/<int:user_id>`
- **Method**: GET
- **Description**: Lists all movies for a specific user.

### Add User
- **URL**: `/add_user`
- **Method**: GET, POST
- **Description**: Displays a form to add a new user and handles form submission.

### Add Movie
- **URL**: `/users/<int:user_id>/add_movie`
- **Method**: GET, POST
- **Description**: Displays a form to add a new movie for a specific user and handles form submission.

### Update Movie
- **URL**: `/users/<int:user_id>/update_movie/<int:movie_id>`
- **Method**: GET, POST
- **Description**: Displays a form to update a specific movie for a specific user and handles form submission.

### Delete Movie
- **URL**: `/users/<int:user_id>/delete_movie/<int:movie_id>`
- **Method**: GET
- **Description**: Deletes a specific movie from a user's list.

### Error Handling

#### 404 Error
- **URL**: Any non-existent route
- **Method**: GET
- **Description**: Displays a custom 404 error page.

