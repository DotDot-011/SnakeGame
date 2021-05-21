class Error(Exception):

    pass

class CannotAddLadder(Error):

    def __init__(self, message: str) -> None:
        self.message = message

class CannotAddSnake(Error):

    def __init__(self, message: str) -> None:
        self.message = message
        