import random
import movie_storage as ms


def my_moviesDB():
    # Application's control Interface that allows user
    # selection of operations to run

    selections = """
  ********** My Movies Database **********

  Menu:
  0. Exit
  1. List movies
  2. Add movie
  3. Delete movie
  4. Update movie
  5. Stats
  6. Random movie
  7. Search movie
  8. Movies sorted by rating
  9. Generate Website

  """
    print(selections)
    choice = input("Enter choice (0-9): ")
    while choice not in choice_dict.keys():
        print(selections)
        choice = input("Enter choice (0-9): ")
    choice_dict[choice]()


def list_movies():
    """Displays the list of movies"""
    movies = ms.list_movies()
    print()
    print(f"  {len(movies)} movies in total")
    for movie in movies:
        print(f"  {movie['Title']}: {movie['Rating']}")
    con = input("""
  Press enter to continue: """)
    my_moviesDB()


def add_movie():
    """Adds a new movie to the dictionary"""
    movies = ms.list_movies()
    new_movie = input("Enter new movie name: ")
    for movie in movies:
        if new_movie in movie.values():
            print(
                f"Error: The movie {new_movie} already exists in the database.")
            add_movie()
    rating = float(input("Enter new movie rating (1-10): "))
    release_year = float(input("Enter the movie's release year: "))
    ms.add_movie(new_movie, release_year, rating)
    con = input("""Press enter to continue: """)
    my_moviesDB()


def del_movie():
    """ Deletes a movie from the database """
    title = input("Enter movie name to delete: ")
    ms.delete_movie(title)
    return_to_menu()


def update_movie():
    # Updates the movie's rating
    movies = ms.list_movies()
    title = input("Enter movie name: ")
    # checks if movie exists in dictionary
    for movie in movies:
        if movie['Title'] == title:
            rating = float(input("Enter new movie rating (1-10): "))
            ms.update_movie(title, rating)
    return_to_menu()


def return_to_menu():
    # Returns the app to the menu of operations
    print(" ")
    con = input("Press enter to continue: ")
    my_moviesDB()


def check_stats():
    # Displays movie stats based on the ratings
    movies_lst = ms.list_movies()
    avg_rating = 0
    sum_rating = 0
    median_rating = 0
    sorted_val = []
    movie_ratings = []

    # calculates the average rating
    for movie in movies_lst:
        movie_ratings.append(movie['Rating'])
        sum_rating += movie['Rating']
    avg_rating = sum_rating / len(movies_lst)

    sorted_val = sorted(movie_ratings)
    length = len(sorted_val)
    # for lists with an even number of items
    if length % 2 == 0:
        a = sorted_val[length // 2]
        b = sorted_val[(length//2) - 1]
        c = (a + b) / 2
        median_rating = c
    # for lists with an odd number of items
    if length % 2 > 0:
        median_rating = sorted_val[length//2]

    # evaluates max and min ratings to determine best/worst movie
    best_movie = ""
    worst_movie = ""
    best = max(movie_ratings)
    worst = min(movie_ratings)
    for movie in movies_lst:
        if movie['Rating'] == best:
            best_movie = movie['Title']
        if movie['Rating'] == worst:
            worst_movie = movie['Title']

    # displays summary of stats
    print(f"Average rating: {avg_rating}")
    print(f"Median rating: {median_rating}")
    print(f"Best movie: {best_movie}")
    print(f"Worst movie: {worst_movie}")
    return_to_menu()


def random_movie():
    # selects a random movie from list of dictionary movies
    movies_lst = ms.list_movies()
    rand_movie = random.choice(movies_lst)
    print(
        f"Your movie for tonight: {rand_movie['Title']}, it's rated {rand_movie['Rating']}")
    return_to_menu()


def search_movie():
    # searches for movie titles using full title or substrings
    movies_lst = ms.list_movies()
    movie_name = input("Enter part of movie name: ").lower()
    for i in range(len(movies_lst)):
        name = movies_lst[i]['Title'].lower()
        rating = movies_lst[i]['Rating']
        if name.__contains__(movie_name):
            print(f"{movies_lst[i]['Title']}, {rating}")
    return_to_menu()


def sort_by_rating():
    # sorts movie titles based on ratings in descending order
    movies_lst = ms.list_movies()
    movie_ratings = []
    for movie in movies_lst:
        movie_ratings.append(movie['Rating'])
    sorted_lst = sorted(movie_ratings, key=lambda x: x, reverse=True)
    for rating in sorted_lst:
        for movie in movies_lst:
            if movie['Rating'] == rating:
                print(f"{movie['Title']}: {movie['Rating']}")
    return_to_menu()


def exit_movies():
    stop = 1
    print("Bye!")
    return stop


def generate_website():
    return_to_menu()


choice_dict = {
    "0": exit_movies,
    "1": list_movies,
    "2": add_movie,
    "3": del_movie,
    "4": update_movie,
    "5": check_stats,
    "6": random_movie,
    "7": search_movie,
    "8": sort_by_rating,
    "9": generate_website
}


def main():
    # Your code here
    my_moviesDB()


if __name__ == "__main__":
    main()
