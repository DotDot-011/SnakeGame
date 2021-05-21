class Error(Exception):

    pass

class CannotCreateFinishLine(Error):

    def __init__(self, message: str) -> None:
        self.message = message

class CannotAddLadder(Error):

    def __init__(self, message: str) -> None:
        self.message = message

class CannotAddSnake(Error):

    def __init__(self, message: str) -> None:
        self.message = message
