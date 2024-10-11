movie_1 = {"name":"Inception", "year":2010, "rating":8.7}
movie_2 = {"name":"Inside Out", "year":2015, "rating":8.1}
movie_3 = {"name":"Con Air", "year":1997, "rating":6.9}
movie_4 = {"name":"Movie 4", "year":2005, "rating":8.1}
movie_5 = {"name":"Movie 5", "year":2012, "rating":8.2}

movies = [movie_1, movie_2, movie_3, movie_4, movie_5]
print(movies) # Printer ut en liste for å sjekke innholdet
print("------------------------------------------")

# A) Opprett en funksjon som tar en liste med filmer, og filnavn som parameter.

def add_movie_to_file(movies, filnavn):
    with open(filnavn, 'w') as fil: #åpner eller lagrer fil. 'w'(write) - overskriver innhold.
        for movie in movies:
            text = f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}\n"
            fil.write(text) # skriver teksten til fil

add_movie_to_file(movies, "movies.txt")

# B) Lag en funksjon som leser den samme filen og skriver ut innholdet

def print_file_contents(filnavn):
    with open(filnavn, 'r') as fil: # 'r'(read)
        content = fil.read() # leser innhold i fil
        print(content)

print_file_contents("movies.txt")