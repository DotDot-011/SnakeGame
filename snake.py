from error import *

class Snake:

    def __init__(self, head: int, tail: int, board_size: int) -> None:
        self.check_create_condition(head, tail, board_size)

        self.head = head
        self.tail = tail

    def check_create_condition(self, head: int, tail: int, board_size: int) -> bool:
        if(head <= tail):
            raise HeadSnakeLessThanTailError(head, tail)

        if(tail < 1):
            raise TailSnakeLessThanOneError(head, tail)

        if(head >= board_size):
            raise HeadSnakeMoreThanBoardSizeError(head, tail)
