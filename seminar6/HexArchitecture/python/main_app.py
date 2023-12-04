from seminar6.HexArchitecture.python.adapters import MovieReviewsRepo, ConsolePrinter, UserCommand
from seminar6.HexArchitecture.python.application import MovieUser
from seminar6.HexArchitecture.python.domain import MovieSearchRequest

if __name__ == "__main__":
    # Обращаемся к базе с фильмами через порт-адаптер <<i_fetch_movie_review>> <<movie_reviews_repo>>
    fetch_movie_reviews = MovieReviewsRepo()
    # Создаем подключение к консольному принтеру через порт-адаптер <<i_print_movie_reviews.py>> <<console_printer>>
    print_movie_reviews = ConsolePrinter()
    # Предоставление пользователю базы и принтера посредством порта-адаптера <<i_user_input>> <<user_command>>
    user_command = UserCommand(fetch_movie_reviews, print_movie_reviews)

    # Создание пользовательского приложения для чтения обзоров
    movie_user = MovieUser(user_command)

    for film in 'StarWars', 'StarTrack', 'StarField':
        # Поиск фильма
        film_request = MovieSearchRequest(film)
        print(f'Displaying reviews for movie: {film}')
        # Обзоры на этот фильм
        movie_user.process_input(film_request)
