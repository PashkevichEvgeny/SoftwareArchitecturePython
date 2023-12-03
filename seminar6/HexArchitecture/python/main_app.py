from adapters.console_printer import ConsolePrinter
from adapters.movie_reviews_repo import MovieReviewsRepo
from adapters.user_command import UserCommand
from application.movie_user import MovieUser
from domain.movie_search_request import MovieSearchRequest


if __name__ == "__main__":
    # Обращаемся к базе с фильмами через порт-адаптер <<i_fetch_movie_review>> <<movie_reviews_repo>>
    fetchMovieReviews = MovieReviewsRepo()
    # Создаем подключение к консольному принтеру через порт-адаптер <<i_print_movie_reviews.py>> <<console_printer>>
    printMovieReviews = ConsolePrinter()
    # Предоставление пользователю базы и принтера посредством порта-адаптера <<i_user_input>> <<user_command>>
    userCommand = UserCommand(fetchMovieReviews, printMovieReviews)

    # Создание пользовательского приложения для чтения обзоров
    movieUser = MovieUser(userCommand)

    for film in "StarWars", "StarTrack":
        # Поиск фильма
        filmRequest = MovieSearchRequest(film)
        print("Displaying reviews for movie " + filmRequest.getMovieName)
        # Обзоры на этот фильм
        movieUser.processInput(filmRequest)
