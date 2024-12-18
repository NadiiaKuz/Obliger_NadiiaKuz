movie_1 = {"name":"Inception", "year":2010, "rating":8.7}
movie_2 = {"name":"Inside Out", "year":2015, "rating":8.1}
movie_3 = {"name":"Con Air", "year":1997, "rating":6.9}
movie_4 = {"name":"Movie 4", "year":2005, "rating":8.1}
movie_5 = {"name":"Movie 5", "year":2012, "rating":8.2}

movies = [movie_1, movie_2, movie_3, movie_4, movie_5]
print(movies) # Printer ut en liste for å sjekke innholdet
print("------------------------------------------")

# A) Lag en funksjon som printer ut alle filmene i en gitt liste

def print_movies(movies):
    for movie in movies:
        print(f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}")

print_movies(movies)
print("------------------------------------------")

# B) Lag en funksjon som tar en liste med filmer som parameter
# og regner ut gjennomsnittsratingen for alle filmene i lista og returnerer dette.

def count_average_movie_rating(movies):
    average_rating = 0
    for movie in movies:
        average_rating += movie["rating"] / len(movies)
    return average_rating.__round__(1)

print(f"Gjennomsnittsratingen er {count_average_movie_rating(movies)}")
print("------------------------------------------")

# C) Lag en funksjon som tar en liste med filmer og et årstall som parametere,
# og returnerer en ny liste med alle filmer fra og med det gitte årstallet.

def select_movies_by_year(movies, year):
    new_movies = []
    for movie in movies:
        if (movie["year"] >= year):
            new_movies.append(movie)
    return new_movies

movie_from_2010 = select_movies_by_year(movies, 2010)
print_movies(movie_from_2010)