from typing import List
from seminar6.HexArchitecture.python.domain.movie_review import MovieReview
from seminar6.HexArchitecture.python.domain.movie_search_request import MovieSearchRequest
from seminar6.HexArchitecture.python.ports.i_fetch_movie_reviews import iFetchMovieReviews


class MovieReviewsRepo(iFetchMovieReviews):
    def __init__(self):
        self.movieReviewMap = {}
        self.initialize()


    def fetchMovieReviews(self, movieSearchRequest: MovieSearchRequest) -> List[MovieReview]:
        return self.movieReviewMap.get(movieSearchRequest.getMovieName, [])

    def initialize(self):
        self.movieReviewMap = {
            "StarWars": [MovieReview("1", 7.5, "Good")],
            "StarTrack": [MovieReview("1", 8.0, "Good"),
                          MovieReview("2", 9.6, "Excellent"),
                          MovieReview("3", 9.5, "Excellent"),
                          MovieReview("4", 9.2, "Excellent"),
                          MovieReview("5", 8.5, "Good")]
        }