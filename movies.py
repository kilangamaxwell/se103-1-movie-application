import random

def my_moviesDB(movies_dict):
  #Application's control Interface that allows user 
  #selection of operations to run

  selections = """
  ********** My Movies Database **********

  Menu:
  1. List movies
  2. Add movie
  3. Delete movie
  4. Update movie
  5. Stats
  6. Random movie
  7. Search movie
  8. Movies sorted by rating

  """
  print(selections)
  choice = int(input("Enter choice (1-8): "))
  while choice not in range(1,9):
    print(selections)
    choice = int(input("Enter choice (1-8): "))
  if choice == 1:
    list_movies(movies_dict)
  if choice == 2:
    add_movie(movies_dict)
  if choice == 3:
    del_movie(movies_dict)
  if choice == 4:
    update_movie(movies_dict)
  if choice == 5:
    check_stats(movies_dict)
  if choice == 6:
    random_movie(movies_dict)
  if choice == 7:
    search_movie(movies_dict)
  if choice == 8:
    sort_by_rating(movies_dict)
  

def list_movies(movies_dict):
  #Displays the list of movies in the dictionary
  print(f"  {len(movies_dict.keys())} movies in total")
  for key in movies_dict:
    print(f"  {key}: {movies_dict[key]}")
  con = input("""
  Press enter to continue: """)
  my_moviesDB(movies_dict)

def add_movie(movies_dict):
  #Adds a new movie to the dictionary
  new_movie = input("Enter new movie name: ")
  rating = int(input("Enter new movie rating (1-10): "))
  movies_dict[new_movie] = rating
  print(f"Movie {new_movie} successfully added")
  print(" ")
  con = input("""Press enter to continue: """)
  my_moviesDB(movies_dict)

def del_movie(movies_dict):
  #Deletes a movie from the dictionary
  movie_name = input("Enter movie name to delete: ")
  if movie_name not in movies_dict.keys():
    print(f"Movie {movie_name} doesn't exist!")
    return_to_menu(movies_dict)
  else:
    del movies_dict[movie_name]
    print(f"Movie {movie_name} successfully deleted")
    return_to_menu(movies_dict)

def update_movie(movies_dict):
  #Updates the movie's rating
  movie_name = input("Enter movie name: ")
  #checks if movies exists in dictionary
  if movie_name not in movies_dict.keys():
    print(f"Movie {movie_name} doesn't exist!")
    return_to_menu(movies_dict)
  else:
    rating = int(input("Enter new movie rating (1-10): "))
    movies_dict[movie_name] = rating
    print(f"Movie {movie_name} successfully updated")
    return_to_menu(movies_dict)

def return_to_menu(movies_dict):
  #Returns the app to the menu of operations
  print(" ")
  con = input("Press enter to continue: ")
  my_moviesDB(movies_dict)

def check_stats(movies_dict):
  #Displays movie stats based on the ratings
  avg_rating = 0
  sum_rating = 0
  median_rating = 0
  sorted_val = []

  #calculates the average rating
  for val in movies_dict.values():
    sum_rating += val
  avg_rating = sum_rating / len(movies_dict.values())

  sorted_val = sorted(movies_dict.values())
  length = len(sorted_val)
  #for lists with an even number of items
  if length % 2 == 0:
    a = sorted_val[length // 2]
    b = sorted_val[(length//2) - 1]
    c = (a + b) / 2
    median_rating = c
  #for lists with an odd number of items
  if length % 2 > 0:
    median_rating = sorted_val[length//2]
  
  #evaluates max and min ratings to determine best/worst movie
  best_movie = ""
  worst_movie = ""
  best = max(movies_dict.values())
  worst = min(movies_dict.values())
  for key in movies_dict:
    if movies_dict[key] == best:
      best_movie = key
    if movies_dict[key] == worst:
      worst_movie = key
  
  #displays summary of stats
  print(f"Average rating: {avg_rating}")
  print(f"Median rating: {median_rating}")
  print(f"Best movie: {best_movie}")
  print(f"Worst movie: {worst_movie}")
  return_to_menu(movies_dict)

def random_movie(movies_dict):
  #selects a random movie from list of dictionary tuples
  movie, rating = random.choice(list(movies_dict.items()))
  print(f"Your movie for tonight: {movie}, it's rated {rating}")
  return_to_menu(movies_dict)

def search_movie(movies_dict):
  #searches for movie titles using full title or substrings
  movie_name = input("Enter part of movie name: ")
  movie_name = movie_name.lower()
  for key in movies_dict.keys():
    if movie_name in key.lower():
      print(f"{key}, {movies_dict[key]}")
  return_to_menu(movies_dict)

def sort_by_rating(movies_dict):
  #sorts movie titles based on ratings in descending order
  sorted_lst = sorted(movies_dict.items(), key=lambda x: x[1], reverse=True)
  for pair in sorted_lst:
    for key in movies_dict:
      if movies_dict[key] == pair[1]:
        print(f"{key}: {pair[1]}")
  return_to_menu(movies_dict)

def main():
  # Dictionary to store the movies and the rating
  movies = {
      "The Shawshank Redemption": 9.5,
      "Pulp Fiction": 8.8,
      "The Room": 3.6,
      "The Godfather": 9.2,
      "The Godfather: Part II": 9.0,
      "The Dark Knight": 9.0,
      "12 Angry Men": 8.9,
      "Everything Everywhere All At Once": 8.9,
      "Forrest Gump": 8.8,
      "Star Wars: Episode V": 8.7
  }

  # Your code here
  my_moviesDB(movies)
    
    

if __name__ == "__main__":
  main()
