class Error(Exception):

    pass

class StartLadderMoreThanFinishError(Error):

    def __init__(self, start: int, finish: int) -> None:
        self.message = self.create_message(start, finish)

    def create_message(self, start: int, finish: int) -> str:
        return f"Ladder start: {start}, finish: {finish}, start of this ladder more than Finish" 

class StartLadderLessThanOneError(Error):
    
    def __init__(self, start: int, finish: int) -> None:
        self.message = self.create_message(start, finish)

    def create_message(self, start: int, finish: int) -> str:
        return f"Ladder start: {start}, finish: {finish}, start {start} is less than 1"

class FinishLadderMoreThanBoardSizeError(Error):

    def __init__(self, start: int, finish: int) -> None:
        self.message = self.create_message(start, finish)

    def create_message(self, start: int, finish: int) -> str:
        return f"Ladder start: {start}, finish: {finish}, finish {finish} is more than board size"

class HeadSnakeLessThanTailError(Error):

    def __init__(self, head: int, tail: int) -> None:
        self.message = self.create_message(head, tail)

    def create_message(self, head: int, tail: int) -> str:
        return f"Snake head: {head}, tail: {tail}, head of this snake less than tail"

class TailSnakeLessThanOneError(Error):

    def __init__(self, head: int, tail: int) -> None:
        self.message = self.create_message(head, tail)

    def create_message(self, head: int, tail: int) -> str:
        return f"Snake head: {head}, tail: {tail}, tail {tail} is less than 1"

class HeadSnakeMoreThanBoardSizeError(Error):

    def __init__(self, head: int, tail: int) -> None:
        self.message = self.create_message(head, tail)

    def create_message(self, head: int, tail: int) -> str:
        return f"Snake head: {head}, tail: {tail}, head {head} is more than board size"

class BoardSizeLessThanOneError(Error):

    def __init__(self, board_size: int) -> None:
        self.message = self.create_message(board_size)

    def create_message(self, board_size: int) -> str:
        return f"Board size {board_size} is less than one"

class BoardSizeEqualStartError(Error):

    def __init__(self, board_size: int) -> None:
        self.message = self.create_message(board_size)

    def create_message(self, board_size: int) -> str:
        return f"Board size {board_size} is equal to start line"

class FinishLineMoreThanBoardSizeError(Error):

    def __init__(self, board_size: int, finish_line: int) -> None:
        self.message = self.create_message(board_size, finish_line)

    def create_message(self, board_size: int, finish_line: int) -> str:
        return f"Finish line {finish_line} is more than Board size {board_size}"

class FinishLineLessThanOneError(Error):

    def __init__(self, finish_line: int) -> None:
        self.message = self.create_message(finish_line)

    def create_message(self, finish_line: int) -> str:
        return f"Finish line {finish_line} is less than 1"

class FinishLineEqualStartError(Error):
    
    def __init__(self, finish_line: int) -> None:
        self.message = self.create_message(finish_line)

    def create_message(self, finish_line: int) -> str:
        return f"Finish line {finish_line} is equal to start line"

class NewStartLadderEqualStartLadderError(Error):

    def __init__(self, chained_ladder_start: int, chained_ladder_finish: int, new_ladder_start: int) -> None:
        self.message = self.create_message(chained_ladder_start, chained_ladder_finish, new_ladder_start)

    def create_message(self, chained_ladder_start: int, chained_ladder_finish: int, new_ladder_start: int) -> str:
        return f"Ladder start: {new_ladder_start} equal to start lader with start: {chained_ladder_start} finish: {chained_ladder_finish}"

class NewStartLadderChainFinishLadderError(Error):

    def __init__(self, chained_ladder_start: int, chained_ladder_finish: int, new_ladder: int) -> None:
        self.message = self.create_message(chained_ladder_start, chained_ladder_finish, new_ladder)

    def create_message(self, chained_ladder_start: int, chained_ladder_finish: int, new_ladder_start: int) -> str:
        return f"Ladder start: {new_ladder_start} chain to finish lader start: {chained_ladder_start} finish: {chained_ladder_finish}"

class NewFinishLadderChainStartLadderError(Error):

    def __init__(self, chained_ladder_start: int, chained_ladder_finish: int, new_ladder_finish: int) -> None:
        self.message = self.create_message(chained_ladder_start, chained_ladder_finish, new_ladder_finish)

    def create_message(self, chained_ladder_start: int, chained_ladder_finish: int, new_ladder_finish: int) -> str:
        return f"Ladder finish: {new_ladder_finish} chain to start lader with start: {chained_ladder_start} finish: {chained_ladder_finish}"

class NewStartLadderEqualHeadSnakeError(Error):

    def __init__(self, chained_snake_head: int, chained_snake_tail: int, new_ladder_start: int) -> None:
        self.message = self.create_message(chained_snake_head, chained_snake_tail, new_ladder_start)

    def create_message(self, chained_snake_head: int, chained_snake_tail: int, new_ladder_start: int) -> str:
        return f"Ladder start: {new_ladder_start} equal to head snake with head: {chained_snake_head} tail: {chained_snake_tail}"

class NewStartLadderChainTailSnakeError(Error):

    def __init__(self, chained_snake_head: int, chained_snake_tail: int, new_ladder_start: int) -> None:
        self.message = self.create_message(chained_snake_head, chained_snake_tail, new_ladder_start)

    def create_message(self, chained_snake_head: int, chained_snake_tail: int, new_ladder_start: int) -> str:
        return f"Ladder start: {new_ladder_start} chain to tail snake with head: {chained_snake_head} tail: {chained_snake_tail}"

class NewFinishLadderChainHeadSnakeError(Error):

    def __init__(self, chained_snake_head: int, chained_snake_tail: int, new_ladder_finish: int) -> None:
        self.message = self.create_message(chained_snake_head, chained_snake_tail, new_ladder_finish)

    def create_message(self, chained_snake_head: int, chained_snake_tail: int, new_ladder_finish: int) -> str:
        return f"Ladder finish: {new_ladder_finish} chain to head snake with head: {chained_snake_head} tail: {chained_snake_tail}"

class NewHeadSnakeEqualStartLadderError(Error):

    def __init__(self, chained_ladder_start: int, chained_ladder_finish: int, new_snake_head: int) -> None:
        self.message = self.create_message(chained_ladder_start, chained_ladder_finish, new_snake_head)

    def create_message(self, chained_ladder_start: int, chained_ladder_finish: int, new_snake_head: int) -> str:
        return f"Snake head: {new_snake_head} equal to start ladder with start: {chained_ladder_start} finish: {chained_ladder_finish}"

class NewHeadSnakeChainFinishLadderError(Error):

    def __init__(self, chained_ladder_start: int, chained_ladder_finish: int, new_snake_head: int) -> None:
        self.message = self.create_message(chained_ladder_start, chained_ladder_finish, new_snake_head)

    def create_message(self, chained_ladder_start: int, chained_ladder_finish: int, new_snake_head: int) -> str:
        return f"Snake head: {new_snake_head} chain to finish ladder with start: {chained_ladder_start} finish: {chained_ladder_finish}"

class NewTailSnakeChainStartLadderError(Error):

    def __init__(self, chained_ladder_start: int, chained_ladder_finish: int, new_snake_tail: int) -> None:
        self.message = self.create_message(chained_ladder_start, chained_ladder_finish, new_snake_tail)

    def create_message(self, chained_ladder_start: int, chained_ladder_finish: int, new_snake_tail: int) -> str:
        return f"Snake tail: {new_snake_tail} chain to start ladder with start: {chained_ladder_start} finish: {chained_ladder_finish}"

class NewHeadSnakeEqualHeadSnakeError(Error):

    def __init__(self, chained_snake_head: int, chained_snake_tail: int, new_snake_head: int) -> None:
        self.message = self.create_message(chained_snake_head, chained_snake_tail, new_snake_head)

    def create_message(self, chained_snake_head: int, chained_snake_tail: int, new_snake_head: int) -> str:
        return f"Snake head: {new_snake_head} equal to head snake with head: {chained_snake_head} tail: {chained_snake_tail}"

class NewHeadSnakeChainTailSnakeError(Error):

    def __init__(self, chained_snake_head: int, chained_snake_tail: int, new_snake_head: int) -> None:
        self.message = self.create_message(chained_snake_head, chained_snake_tail, new_snake_head)

    def create_message(self, chained_snake_head: int, chained_snake_tail: int, new_snake_head: int) -> str:
        return f"Snake head: {new_snake_head} chain to tail snake with head: {chained_snake_head} tail: {chained_snake_tail}"

class NewTailSnakeChainHeadSnakeError(Error):

    def __init__(self, chained_snake_head: int, chained_snake_tail: int, new_snake_tail: int) -> None:
        self.message = self.create_message(chained_snake_head, chained_snake_tail, new_snake_tail)

    def create_message(self, chained_snake_head: int, chained_snake_tail: int, new_snake_tail: int) -> str:
        return f"Snake tali: {new_snake_tail} chain to head snake with head: {chained_snake_head} tail: {chained_snake_tail}"
