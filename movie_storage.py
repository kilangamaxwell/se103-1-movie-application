import json


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
    with open("movies.json", "r") as jfile:
        movies_lst = json.load(jfile)
        return movies_lst


def save_db(movies):
    saved = 0
    moviesdb = json.dumps(movies)
    with open("movies.json", "w") as jfile:
        jfile.write(moviesdb)
        saved = 1
    return saved


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    movies.append({
        'Title': title,
        'Rating': rating,
        'Year': year
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
    for i in range(len(movies)):
        if movies[i]['Title'] == title:
            del movies[i]
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
