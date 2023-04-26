import json
movies = [
    {
        "Title": "In the Name of the Father",
        "Rating": 8.1,
        "Year": 1993
    },
    {
        "Title": "Titanic",
        "Rating": 7.9,
        "Year": 1997
    },
    {
        "Title": "Deadpool",
        "Rating": 8.0,
        "Year": 2016
    }
]


def main():
    moviedb = json.dumps(movies)
    with open("movies.json", "w") as jfile:
        jfile.write(moviedb)


if __name__ == "__main__":
    main()
