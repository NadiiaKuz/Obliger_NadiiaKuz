# A) Opprett en klasse for filmer med inneholder instansvariabler for filmtittel, utgivelsesår og score.

class Movie:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score

# B) Opprett en metode i filmklassen som returnerer en tekststreng med all informasjon om en gitt film
    def get_movie_info(self):
        return f"{self.title} was released in {self.year} and currently has a score of {self.score}"



movie_1 = Movie("Inception", 2010, 8.8)
movie_2 = Movie("The Martian", 2010, 8.0)
movie_3 = Movie("Joker", 2019, 8.4)

print(f"{movie_1.title} was released in {movie_1.year} and currently has a score of {movie_1.score}")
print(f"{movie_2.title} was released in {movie_2.year} and currently has a score of {movie_2.score}")
print(f"{movie_3.title} was released in {movie_3.year} and currently has a score of {movie_3.score}")

print("---------------------------------------------------------------------------")

print(movie_1.get_movie_info())
print(movie_2.get_movie_info())
print(movie_3.get_movie_info())