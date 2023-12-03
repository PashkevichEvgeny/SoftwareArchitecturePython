class MovieSearchRequest:

    def __init__(self, name):
        self.request = name

    @property
    def getMovieName(self):
        return self.request
