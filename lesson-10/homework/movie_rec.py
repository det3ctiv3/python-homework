import requests
import random

api_key = "frfrrfrfrfrfrfr"

genres = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "sci-fi": 878,
    "romance": 10749
}

print("Available genres:", ", ".join(genres.keys()))
user_genre = input("Pick a genre: ").lower()

if user_genre in genres:
    genre_id = genres[user_genre]

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = data["results"]

        if movies:
            movie = random.choice(movies)
            title = movie["title"]
            overview = movie["overview"]

            print(f"\nRecommended {user_genre} movie:")
            print(f"Title: {title}")
            print(f"Overview: {overview}")
        else:
            print("No movies found for that genre. Weird!")
    else:
        print(f"Uh-oh! API error: {response.status_code}. Check your key!")
else:
    print("Sorry, that genre isn’t in my list. Try again!")