import requests
import random


class MovieRecommender:
    def __init__(self, api_key):
        self.api_key = api_key
        self.genres = self.get_genres()

    def get_genres(self):
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}&language=en-US"
        response = requests.get(url)
        if response.status_code == 200:
            genres = response.json()["genres"]
            return {genre["name"].lower(): genre["id"] for genre in genres}
        else:
            print("Error fetching genres.")
            return {}

    def get_movies_by_genre(self, genre_id):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&with_genres={genre_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            print("Error fetching movies.")
            return []

    def recommend_movie(self):
        if not self.genres:
            return

        print("Available genres:")
        for genre in self.genres:
            print(genre.capitalize())

        user_genre = input("Enter a genre: ").strip().lower()
        if user_genre not in self.genres:
            print("Invalid genre!")
            return

        genre_id = self.genres[user_genre]
        movies = self.get_movies_by_genre(genre_id)

        if not movies:
            print("No movies found for this genre.")
            return

        random_movie = random.choice(movies)
        print(f"We recommend: {random_movie['title']} ({random_movie['release_date'][:4]})")


if __name__ == "__main__":
    API_KEY = "5fe23939ff48d0e9fa6ff98d6d95d8ee"
    recommender = MovieRecommender(API_KEY)
    recommender.recommend_movie()
