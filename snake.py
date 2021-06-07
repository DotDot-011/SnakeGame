from error import *


class Snake:

    def __init__(self, head: int, tail: int, board_size: int) -> None:
        self.check_create_condition(head, tail, board_size)

        self.head = head
        self.tail = tail

    def check_head_more_than_tail(self, head: int, tail: int) -> None:
        if(not(head > tail)):
            raise HeadSnakeLessThanTailError(head, tail)

    def check_tail_more_than_zero(self, head: int, tail: int) -> None:
        if(not(tail > 0)):
            raise TailSnakeLessThanOneError(head, tail)

    def check_head_less_than_board_size(self, head: int, tail: int, board_size: int) -> None:
        if(not(head < board_size)):
            raise HeadSnakeMoreThanBoardSizeError(head, tail)

    def check_create_condition(self, head: int, tail: int, board_size: int) -> bool:
        self.check_head_more_than_tail(head, tail)
        self.check_tail_more_than_zero(head, tail)
        self.check_head_less_than_board_size(head, tail, board_size)
