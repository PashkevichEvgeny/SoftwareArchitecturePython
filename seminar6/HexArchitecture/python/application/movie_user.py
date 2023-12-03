from seminar6.HexArchitecture.python.domain import movie_search_request
from seminar6.HexArchitecture.python.ports import i_user_input


class MovieUser:
    def __init__(self, userInputDriverPort: i_user_input):
        self.userInputDriverPort = userInputDriverPort

    def processInput(self, movieSearchRequest: movie_search_request):
        self.userInputDriverPort.handleUserInput(movieSearchRequest)