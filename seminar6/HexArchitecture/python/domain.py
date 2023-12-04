class Model:
    def __init__(self, movie_app):
        self.movie_app = movie_app

    def run(self, user_command):
        self.movie_app.accept(user_command)


class MovieReview:
    def __init__(self, movie_name, movie_score, remark):
        self.movie_name = movie_name
        self.movie_score = movie_score
        self.remark = remark

    def __repr__(self):
        return f' {self.movie_score} {self.remark}'


class MovieSearchRequest:
    def __init__(self, name):
        self.name = name

    @property
    def movie_name(self):
        return self.name
