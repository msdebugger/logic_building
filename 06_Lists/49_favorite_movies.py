"""
Q49: Favorite Movies Create a list of 5 of your favorite movies. Print the first, last, and middle movie from your list using both positive and negative indexing where appropriate.
"""

fav_movies = ["In the mood for love", "Persona", "Dreams","A moment to remember","Asha Joar Majhe"]

middle = len(fav_movies)//2

print(f"{fav_movies[0]}, {fav_movies[-1]}, {fav_movies[middle]}")