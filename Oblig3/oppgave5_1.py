# A)Opprett en liste med filmer (hvor hver film er en egen dictionary med dataene om én film)
from contextlib import nullcontext

movie_1 = {"name":"Inception", "year":2010, "rating":8.7}
movie_2 = {"name":"Inside Out", "year":2015, "rating":8.1}
movie_3 = {"name":"Con Air", "year":1997, "rating":6.9}

movies = [movie_1, movie_2, movie_3]
print(movies) # Printer ut en liste for å sjekke innholdet
print("------------------------------------------")

# B)Opprett en funksjon som legger til en film i filmlisten.
def add_movie(new_movies, name, year, rating):
    movie = {"name":name, "year":year, "rating":rating}
    new_movies.append(movie)
    return new_movies

add_movie(movies, "Movie4", 2000, 7.0)
add_movie(movies, "Movie5", 2001, 7.1)
add_movie(movies, "Movie6", 2002, 7.2)

for movie in movies:
    print(movie)
print("------------------------------------------")

# C)Modifiser funksjonen fra forrige deloppgave
def add_movie(new_movies, name, year, rating = None):
    if (rating is None):
        movie = {"name":name, "year":year, "rating": 5.0}
    else:
        movie = {"name": name, "year": year, "rating": rating}
    new_movies.append(movie)
    return new_movies

add_movie(movies, "Movie7", 2003)
add_movie(movies, "Movie8", 2004, 7.3)
add_movie(movies, "Modie9", 2005)

for movie in movies:
    print(movie)