from typing import List
from seminar6.HexArchitecture.python.domain.movie_review import MovieReview
from seminar6.HexArchitecture.python.ports.i_print_movie_rewiews import iPrintMovieReviews


class ConsolePrinter(iPrintMovieReviews):
    def writeMovieReviews(self, movieReviewList: List[MovieReview]):
        for movieReview in movieReviewList:
            print(movieReview)






