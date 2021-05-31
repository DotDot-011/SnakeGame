from typing import Optional
from ladder import Ladder
from snake import Snake
from error import *

class Board:
    
    def __init__(self,
                 board_size: int, 
                 finish_line: int, 
                 ladder_coordinates: list[tuple[int, int]] = [], 
                 snake_coordinates: list[tuple[int, int]] = [], 
                 start_line: int = 1) -> None:
        self.check_create_condition(board_size, finish_line, start_line)

        self.size = board_size
        self.finish_line = finish_line
        self.start_line = start_line
        # **************
        self.ladders = []
        self.snakes = []

        self.setup_ladders(ladder_coordinates)
        self.setup_snakes(snake_coordinates)

    def check_create_condition(self, board_size: int, finish_line: int, start_line: int) -> None:
        if(board_size < 1):
            raise BoardSizeLessThanOneError(board_size)

        if(board_size == start_line):
            raise BoardSizeEqualStartError(board_size)

        if(finish_line > board_size):
            raise FinishLineMoreThanBoardSizeError(finish_line, board_size)

        if(finish_line < 1):
            raise FinishLineLessThanOneError(finish_line)

        if(finish_line == start_line):
            raise FinishLineEqualStartError(finish_line)

    # TODO: learn reduce
    def setup_ladders(self, ladder_coordinates: list[tuple[int, int]]) -> None:
        ladders = self.create_ladders(ladder_coordinates)
        
        self.add_ladders(ladders)

    def setup_snakes(self, snake_coordinates: list[tuple[int, int]]) -> None:
        snakes = self.create_snakes(snake_coordinates)
        
        self.add_snakes(snakes)

    def add_ladders(self, ladders: list[Ladder]) -> None:
        for ladder in ladders:
            self.add_ladder(ladder)

    def add_snakes(self, snakes: list[Snake]) -> None:
        for snake in snakes:
            self.add_snake(snake)

    def create_ladders(self, ladder_coordinates: list[tuple[int, int]]) -> list[Ladder]:
        return list(map(lambda ladder_coordinate: Ladder(ladder_coordinate[0], ladder_coordinate[1], self.size), ladder_coordinates))

    def create_snakes(self, snake_coordinates: list[tuple[int, int]]) -> list[Ladder]:
        return list(map(lambda snake_coordinate: Snake(snake_coordinate[0], snake_coordinate[1], self.size), snake_coordinates))

    def check_chaining_ladder_with_ladder(self, new_ladder: Ladder) -> None:
        for ladder in self.ladders:
            if(ladder.start == new_ladder.start):
                raise NewStartLadderEqualStartLadderError(ladder.start, ladder.finish, new_ladder.start)
            
            if(ladder.finish == new_ladder.start):
                raise NewStartLadderChainFinishLadderError(ladder.start, ladder.finish, new_ladder.start)

            if(ladder.start == new_ladder.finish):
                raise NewFinishLadderChainStartLadderError(ladder.start, ladder.finish, new_ladder.finish)

    def check_chaining_snake_with_ladder(self, new_ladder: Ladder) -> None:
        for snake in self.snakes:
            if(snake.head == new_ladder.start):
                raise NewStartLadderEqualHeadSnakeError(snake.head, snake.tail, new_ladder.start)

            if(snake.tail == new_ladder.start):
                raise NewStartLadderChainTailSnakeError(snake.head, snake.tail, new_ladder.start)

            if(snake.head == new_ladder.finish):
                raise NewFinishLadderChainHeadSnakeError(snake.head, snake.tail, new_ladder.finish)

    def check_chaining_ladder_with_snake(self, new_snake: Snake) -> list[Ladder]:
        for ladder in self.ladders:
            if(ladder.start == new_snake.head):
                raise NewHeadSnakeEqualStartLadderError(ladder.start, ladder.finish, new_snake.head)

            if(ladder.finish == new_snake.head):
                raise NewHeadSnakeChainFinishLadderError(ladder.start, ladder.finish, new_snake.head)

            if(ladder.start == new_snake.tail):
                raise NewTailSnakeChainStartLadderError(ladder.start, ladder.finish, new_snake.tail)

    def check_chaining_snake_with_snake(self, new_snake: Snake) -> list[Snake]:
        for snake in self.snakes:
            if(snake.head == new_snake.head):
                raise NewHeadSnakeEqualHeadSnakeError(snake.head, snake.finish, new_snake.head)

            if(snake.tail == new_snake.head):
                raise NewHeadSnakeChainTailSnakeError(snake.head, snake.finish, new_snake.head)

            if(snake.head == new_snake.tail):
                raise NewTailSnakeChainHeadSnakeError(snake.head, snake.tail, new_snake.tail)

    def check_add_ladder_condition(self, new_ladder: Ladder) -> None:
        self.check_chaining_ladder_with_ladder(new_ladder)
        self.check_chaining_snake_with_ladder(new_ladder)

    def check_add_snake_condition(self, new_snake: Snake) -> None:
        self.check_chaining_ladder_with_snake(new_snake)
        self.check_chaining_snake_with_snake(new_snake)

    def add_ladder(self, ladder: Ladder) -> None:
        self.check_add_ladder_condition(ladder)

        self.ladders.append(ladder)

    def add_snake(self, snake: Snake) -> None:
        self.check_add_snake_condition(snake)

        self.snakes.append(snake)

    def get_ladder_by_start_on_position(self, position: int) -> Optional[Ladder]:
        ladders = list(filter(lambda ladder: ladder.start == position, self.ladders))

        if(not ladders):
            return None

        return ladders[0]

    def get_snake_by_head_on_position(self, position: int) -> Optional[Snake]:
        snakes = list(filter(lambda snake: snake.head == position, self.snakes))

        if(not snakes):
            return None

        return snakes[0]

    # For testing and checking snake and ladder
    def show_snake(self) -> None:
        print("List of snake:")

        for snake in self.snakes:
            print(f"snake with head: {snake.head}, tail: {snake.tail}")

    def show_ladder(self) -> None:
        print("List of ladder:")

        for ladder in self.ladders:
            print(f"ladder with start: {ladder.start}, finish: {ladder.finish}")
