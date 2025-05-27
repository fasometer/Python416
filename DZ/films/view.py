def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50,"="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:

    @add_title(" Редактирование данных каталога фильмов ")
    def wait_user_answer(self):
        # print("Редактирование данных каталога фильмов".center(4, "="))
        print("Действия с фильмами:"
              "\n1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    @add_title(" Добавление фильма ")
    def add_user_film(self):
        dict_film = {
            '- название': None,
            '- жанр': None,
            '- режиссер': None,
            '- год выпуска': None,
            '- длительность': None,
            '- студия': None,
            '- актеры': None
        }
        # print("Добавление фильма".center(50, "="))
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        # print("=" * 50)
        return dict_film

    @add_title(" Каталог фильмов ")
    def show_all_films(self, films):
        # print("Каталог фильмов ".center(50, "="))
        for ind, fimm in enumerate(films, 1):
            print(f"{ind} {fimm}")
        # print("=" * 50)

    @add_title(" Ввод названия фильма ")
    def get_user_film(self):
        return input("Введите название фильма:")

    @add_title(" Сообщение об ошибке ")
    def show_incorrect_title_error(self,user_title):
        print(f"Фильма с названием \"{user_title}\" не существует")

    @add_title(" Просмотр определенного фильма")
    def show_single_film(self,film):
        for i in film:
            print(f"{i} фильма - {film[i]}")
