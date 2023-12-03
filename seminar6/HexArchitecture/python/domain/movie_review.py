class MovieReview:
 
    def __init__(self, movieName, movieScore, remark):
        self.movieName = movieName
        self.movieScore = movieScore
        self.remark = remark

    def __repr__(self):
        return f' {self.movieScore} {self.remark}'
