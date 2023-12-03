from seminar6.HexArchitecture.python.application.movie_app import MovieApp
from seminar6.HexArchitecture.python.domain.model import Model
from seminar6.HexArchitecture.python.ports.i_fetch_movie_reviews import iFetchMovieReviews
from seminar6.HexArchitecture.python.ports.i_print_movie_rewiews import iPrintMovieReviews
from seminar6.HexArchitecture.python.ports.i_user_input import iUserInput


class UserCommand(iUserInput):
    def __init__(self, fetchMovieReviews: iFetchMovieReviews, printMovieReviews: iPrintMovieReviews):
        movieApp = MovieApp(fetchMovieReviews, printMovieReviews)
        self.model = Model(movieApp)

    def handleUserInput(self, userCommand):
        self.model.Run(userCommand)
