from abc import ABC, abstractmethod
from typing import List, Any

class DataManagerInterface(ABC):
    @abstractmethod
    def get_all_users(self) -> List[Any]:
        """Retrieve all users"""
        pass

    @abstractmethod
    def get_user_movies(self, user_id: int) -> List[Any]:
        """Retrieve movies for a specific user"""
        pass

    @abstractmethod
    def add_user(self, user: Any) -> None:
        """Add a new user"""
        pass

    @abstractmethod
    def add_movie(self, movie: Any) -> None:
        """Add a new movie"""
        pass

    @abstractmethod
    def update_movie(self, movie: Any) -> None:
        """Update an existing movie"""
        pass

    @abstractmethod
    def delete_movie(self, movie_id: int) -> None:
        """Delete a movie by its ID"""
        pass