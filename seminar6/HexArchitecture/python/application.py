from random import shuffle


class MovieApp:
    def __init__(self, movie_repo, movie_console):
        self.movie_repo = movie_repo
        self.movie_console = movie_console

    @staticmethod
    def filter_random_reviews(movie_review_list):
        # Возвращает пять обзоров в случайном порядке
        shuffle(movie_review_list)
        return movie_review_list[:5]

    def accept(self, movie_search_request):
        movie_review_list = self.movie_repo.fetch_movie_reviews(movie_search_request)
        random_reviews = self.filter_random_reviews(movie_review_list)
        self.movie_console.write_movie_reviews(random_reviews)


class MovieUser:
    def __init__(self, user_input_driver_port):
        self.user_input_driver_port = user_input_driver_port

    def process_input(self, movie_search_request):
        self.user_input_driver_port.handle_user_input(movie_search_request)

