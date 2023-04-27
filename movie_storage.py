import json
import requests

JSON_FILE = "OMDB_movies.json"
API_KEY = "d4ba49c2"
URL = "http://www.omdbapi.com/?apikey=d4ba49c2&t="


def list_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data. 

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    with open(JSON_FILE, "r") as jfile:
        movies_lst = json.load(jfile)
        return movies_lst


def save_db(movies):
    saved = 0
    moviesdb = json.dumps(movies)
    with open(JSON_FILE, "w") as jfile:
        jfile.write(moviesdb)
        saved = 1
    return saved


def add_movie(title):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    response = requests.get(URL+title)
    try:
        response = requests.get(URL+title)
        response.raise_for_status()  # Raises an HTTPError for 4xx and 5xx status codes
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
    if response.status_code == requests.codes.ok:
        data = response.json()
    movies.append({
        'Title': data['Title'],
        'Rating': data['imdbRating'],
        'Year': data['Year'],
        'Poster': data['Poster']
    })
    save_db(movies)
    print(f"Movie {title} successfully added")
    print(" ")


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    s = 0
    for movie in movies:
        if movie['Title'] == title:
            movies.remove(movie)
            s = save_db(movies)
    if s == 1:
        print(f"Movie {title} was successfully deleted.")
    else:
        print(f"Movie {title} doesn't exist!")


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    for movie in movies:
        if movie['Title'] == title:
            movie['Rating'] = rating
            s = save_db(movies)
            if s == 1:
                print(f"Movie {title} successfully updated")
            else:
                print(f"Movie {movies} doesn't exist!")
