class Error(Exception):

    pass

# TODO: สร้างฟังชั่นสำหรับ สร้าง error message ภายใน class
class CannotCreateFinishLine(Error):

    def __init__(self, message: str) -> None:
        self.message = message

class CannotAddLadder(Error):

    def __init__(self, message: str) -> None:
        self.message = message

class CannotAddSnake(Error):

    def __init__(self, message: str) -> None:
        self.message = message

class CannotCreateLadder(Error):

    def __init__(self, message: str) -> None:
        self.message = message

class CannotCreateSnake(Error):

    def __init__(self, message: str) -> None:
        self.message = message
