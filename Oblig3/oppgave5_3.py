movie_1 = {"name":"Inception", "year":2010, "rating":8.7}
movie_2 = {"name":"Inside Out", "year":2015, "rating":8.1}
movie_3 = {"name":"Con Air", "year":1997, "rating":6.9}
movie_4 = {"name":"Movie 4", "year":2005, "rating":8.1}
movie_5 = {"name":"Movie 5", "year":2010, "rating":8.2}

movies = [movie_1, movie_2, movie_3, movie_4, movie_5]
print(movies) # Printer ut en liste for å sjekke innholdet
print("------------------------------------------")

# A) Opprett en funksjon som tar en liste med filmer, og filnavn som parameter.

def adding_movie_to_file(movies, filnavn):
    with open(filnavn, 'w') as fil:
        for movie in movies:
            text = f"\n{movie['name']} - {movie['year']} has a riting of {movie['rating']}"
            fil.write(text)

adding_movie_to_file(movies, "movies.txt")

# B) Lag en funksjon som leser den samme filen og skriver ut innholdet

def print_file_contents(filnavn):
    with open(filnavn, 'r') as fil:
        content = fil.read()
        print(content)
print_file_contents("movies.txt")