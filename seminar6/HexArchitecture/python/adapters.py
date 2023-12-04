from typing import List

from seminar6.HexArchitecture.python.application import MovieApp
from seminar6.HexArchitecture.python.domain import MovieReview, MovieSearchRequest, Model
from seminar6.HexArchitecture.python.ports import IPrintMovieReviews, IFetchMovieReviews, IUserInput


class ConsolePrinter(IPrintMovieReviews):
    def write_movie_reviews(self, movie_review_list: List[MovieReview]):
        print(*movie_review_list, sep='\n')


class MovieReviewsRepo(IFetchMovieReviews):
    def __init__(self):
        self.movie_review_map = {}
        self.initialize()

    def fetch_movie_reviews(self, movie_search_request: MovieSearchRequest) -> List[MovieReview]:
        return self.movie_review_map.get(movie_search_request.movie_name, [' Film not found'])

    def initialize(self):
        self.movie_review_map = {
            'StarWars': [
                 MovieReview('1', 7.5, 'Good')],
            'StarTrack': [
                 MovieReview('1', 8.0, 'Good'),
                 MovieReview('2', 9.6, 'Excellent'),
                 MovieReview('3', 9.5, 'Excellent'),
                 MovieReview('4', 9.2, 'Excellent'),
                 MovieReview('5', 8.5, 'Good')]
        }


class UserCommand(IUserInput):
    def __init__(self, movie_repo: IFetchMovieReviews, movie_console: IPrintMovieReviews):
        movie_app = MovieApp(movie_repo, movie_console)
        self.model = Model(movie_app)

    def handle_user_input(self, user_command: MovieSearchRequest):
        self.model.run(user_command)
