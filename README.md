# se103-1-movie-application

Living in a Movie
You’re now going to start your first project 🎊
This exercise is the first step of the project. In the upcoming units you’ll take the code that you wrote here and extend it to support additional features.
Overview

We’re building a movie application. Your movie application will store movie names and their ratings.
You will communicate with the user via a command line, i.e., you print information to the terminal and expect user input.
Your application will support two types of commands:
1. CRUD - Create, Read, Update, Delete
Almost every application implements CRUD commands, since you want to add movies (Create), view the existing movies (Read), update movies (Update), and delete movies (Delete).
You can read more about CRUD in this link, or just Google it.
2. Analytics
Analytics, such as getting the top-rated movie, the least-rated movie etc.

Specification
Movie Data Structure
You will store the movies in a dictionary, provided to you in the skeleton file movies.py. Each key in the dictionary stores the movie name, and each value stores the movie’s rating.
Menu
When opening the application on the first time, your application should display a title of your application (for example, My Movies Database).
After the title, a menu should be displayed with the different options in your applications. Each menu item is printed with a number next to it. Then, the user is requested to enter a choice from the menu.
For example:
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

Enter choice (1-8): 
When the user enters a choice, the command is executed, and then the menu is displayed again so the user can select more options.
Note about the menu
Don’t forget to display the menu again after the command is executed. We want our user to be able to execute multiple commands.
For example, the user can add a movie and then list all the movies.
