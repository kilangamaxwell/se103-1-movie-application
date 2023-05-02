import json
import requests
from bs4 import BeautifulSoup

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
    """Saves the list of movies to a json file."""
    saved = 0
    moviesdb = json.dumps(movies)
    with open(JSON_FILE, "w") as jfile:
        jfile.write(moviesdb)
        saved = 1
    return saved


def find_imdb_link():
    """Retrieves link to imdb page for each movie."""
    url = 'https://imdb.com/chart/top'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html5lib')
    movie_tags = soup.find_all('td', class_='titleColumn')
    movies_tl = []
    for tag in movie_tags:
        title = tag.find('a').text
        link = 'https://imdb.com' + tag.find('a')['href']
        movies_tl.append({
            'Title': title,
            'link': link
        })
    return movies_tl


def find_movie_in_api(title):
    """Retrieves movie info from the OMDB api."""
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
    return data


def add_movie(title):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    data = find_movie_in_api(title)
    movies_tl = find_imdb_link()
    imdbLink = ""
    if data['Country'].__contains__(","):
        country = data['Country'].split(",")
    else:
        country = [data['Country']]
    for mvs in movies_tl:
        if title in mvs['Title']:
            imdbLink = mvs['link']
    if len(imdbLink) > 0:
        movies.append({
            'Title': data['Title'],
            'Rating': data['imdbRating'],
            'Year': data['Year'],
            'Poster': data['Poster'],
            'imdb Link': imdbLink,
            'Notes': [data['Plot']],
            'Country': country
        })
        save_db(movies)
        print(f"Movie {title} successfully added")
    else:
        print("Movie not in imdb top 250")
        movies.append({
            'Title': data['Title'],
            'Rating': data['imdbRating'],
            'Year': data['Year'],
            'Poster': data['Poster'],
            'Country': country
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


def update_movie(title, notes):
    """
    Updates notes about a movie in the database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()
    for movie in movies:
        if movie['Title'] == title:
            movie['Notes'] = notes
            s = save_db(movies)
            if s == 1:
                print(f"Movie {title} successfully updated")
            else:
                print(f"Movie {movies} doesn't exist!")
