from abc import ABC, abstractmethod


class IFetchMovieReviews(ABC):
    @abstractmethod
    def fetch_movie_reviews(self, movie_search_request):
        """ Извлекает из словаря список найденных обзоров"""


class IPrintMovieReviews(ABC):
    @abstractmethod
    def write_movie_reviews(self, movie_review_list):
        """ Распечатывает список обзоров """


class IUserInput(ABC):
    @abstractmethod
    def handle_user_input(self, user_command):
        """ Принимает пользовательский запрос """
