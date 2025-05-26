class UserInterface:

    def wait_user_answer(self):
        print("Редактирование данных каталога фильмов".center(4, "="))
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильма")
        print("q - выход из программы")
        print("Выберите вариант действия: ")
        print("=" * 50)

    def add_user_film(self):
        dict_film = {
            '- название фильма': None,
            '- жанр': None,
            '- режиссер': None,
            '- год выпуска': None,
            '- длительность': None,
            '- студия': None,
            '- актеры': None
        }
        print("Добавление фильма".center(50, "="))
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        print("=" * 50)
        return dict_film

    def show_all_films(self, films):
        print("Каталог фильмов ".center(50, "="))
        for ind, fimm in enumerate(films, 1):
            print(f"{ind} {fimm}")
        print("=" * 50)
