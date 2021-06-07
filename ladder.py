from error import *


class Ladder:

    def __init__(self, start: int, finish: int, board_size: int) -> None:
        self.check_create_condition(start, finish, board_size)
        
        self.start = start
        self.finish = finish

    def check_start_less_than_finish(self, start: int, finish: int) -> None:
        if(not(start < finish)):
            raise StartLadderMoreThanFinishError(start, finish)

    def check_start_more_than_zero(self, start: int, finish: int) -> None:
        if(not(start > 0)):
            raise StartLadderLessThanOneError(start, finish)

    def check_finish_less_than_board_size(self, start: int, finish: int, board_size: int) -> None:
        if(not(finish < board_size)):
            raise FinishLadderMoreThanBoardSizeError(start, finish)        

    def check_create_condition(self, start: int, finish: int, board_size: int) -> bool:
        self.check_start_less_than_finish(start, finish)
        self.check_start_more_than_zero(start, finish)
        self.check_finish_less_than_board_size(start, finish, board_size)
