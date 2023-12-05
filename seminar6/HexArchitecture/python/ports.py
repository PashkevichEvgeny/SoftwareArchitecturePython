from typing import Protocol


class IFetchMovieReviews(Protocol):
    def fetch_movie_reviews(self, movie_search_request):
        """ Извлекает из словаря список найденных обзоров"""


class IPrintMovieReviews(Protocol):
    def write_movie_reviews(self, movie_review_list):
        """ Распечатывает список обзоров """


class IUserInput(Protocol):
    def handle_user_input(self, user_command):
        """ Принимает пользовательский запрос """
