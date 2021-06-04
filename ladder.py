from error import *


class Ladder:

    def __init__(self, start: int, finish: int, board_size: int) -> None:
        self.check_create_condition(start, finish, board_size)
        
        self.start = start
        self.finish = finish

    def check_create_condition(self, start: int, finish: int, board_size: int) -> bool:
        if(start >= finish):
            raise StartLadderMoreThanFinishError(start, finish)

        if(start < 1):
            raise StartLadderLessThanOneError(start, finish)

        if(finish > board_size):
            raise FinishLadderMoreThanBoardSizeError(start, finish)

