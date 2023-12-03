from random import shuffle

from seminar6.HexArchitecture.python.domain.movie_search_request import MovieSearchRequest


class MovieApp:
    def __init__(self, fetchMovieReviews, printMovieReviews):
        self.fetchMovieReviews = fetchMovieReviews
        self.printMovieReviews = printMovieReviews

    def filterRandomReviews(self, movieReviewList):
        shuffle(movieReviewList)
        return movieReviewList

    def accept(self, movieSearchRequest: MovieSearchRequest):
        movieReviewList = self.fetchMovieReviews.fetchMovieReviews(movieSearchRequest)
        randomReviews = self.filterRandomReviews(list(movieReviewList))
        self.printMovieReviews.writeMovieReviews(randomReviews)