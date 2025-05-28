class Film:
    def __init__(self, title, genre, author, year, length, atelier, actors):
        self.title = title
        self.genre = genre
        self.author = author
        self.year = year
        self.length = length
        self.atelier = atelier
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.author})"


class FilmModel:
    def __init__(self):
        self.films = {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()
