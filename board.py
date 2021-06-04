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
        self.ladders = self.__setup_ladders(ladder_coordinates)
        self.snakes = self.__setup_snakes(snake_coordinates)

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

    def __setup_ladders(self, ladder_coordinates: list[tuple[int, int]]) -> list[Ladder]:
        ladders = []
        
        for ladder_coordinate in ladder_coordinates:
            try:
                ladder = Ladder(ladder_coordinate[0], ladder_coordinate[1], self.size)

                self.check_chaining_ladder_with_ladder(ladder, ladders)

                ladders.append(ladder)
                    
            except Error as Er:
                print(Er.message)
                
        return ladders

    def __setup_snakes(self, snake_coordinates: list[tuple[int, int]]) -> list[Snake]:
        snakes = []
        
        for snake_coordinate in snake_coordinates:
            try:
                snake = Snake(snake_coordinate[0], snake_coordinate[1], self.size)

                self.check_chaining_ladder_with_snake(snake, self.ladders)
                self.check_chaining_snake_with_snake(snake, snakes)

                snakes.append(snake)
            
            except Error as Er:
                print(Er.message)
                
        return snakes

    # TODO: merge error with same argument
    def check_chaining_ladder_with_ladder(self, new_ladder: Ladder, ladders: list[Ladder] = []) -> None:
        for ladder in ladders:
            if(ladder.start == new_ladder.start):
                raise NewStartLadderEqualStartLadderError(ladder.start, ladder.finish, new_ladder.start)
            
            if(ladder.finish == new_ladder.start):
                raise NewStartLadderChainFinishLadderError(ladder.start, ladder.finish, new_ladder.start)

            if(ladder.start == new_ladder.finish):
                raise NewFinishLadderChainStartLadderError(ladder.start, ladder.finish, new_ladder.finish)

    def check_chaining_snake_with_ladder(self, new_ladder: Ladder, snakes: list[Snake] = []) -> None:
        for snake in snakes:
            if(snake.head == new_ladder.start):
                raise NewStartLadderEqualHeadSnakeError(snake.head, snake.tail, new_ladder.start)

            if(snake.tail == new_ladder.start):
                raise NewStartLadderChainTailSnakeError(snake.head, snake.tail, new_ladder.start)

            if(snake.head == new_ladder.finish):
                raise NewFinishLadderChainHeadSnakeError(snake.head, snake.tail, new_ladder.finish)

    def check_chaining_ladder_with_snake(self, new_snake: Snake, ladders: list[Ladder] = []) -> list[Ladder]:
        for ladder in ladders:
            if(ladder.start == new_snake.head):
                raise NewHeadSnakeEqualStartLadderError(ladder.start, ladder.finish, new_snake.head)

            if(ladder.finish == new_snake.head):
                raise NewHeadSnakeChainFinishLadderError(ladder.start, ladder.finish, new_snake.head)

            if(ladder.start == new_snake.tail):
                raise NewTailSnakeChainStartLadderError(ladder.start, ladder.finish, new_snake.tail)

    def check_chaining_snake_with_snake(self, new_snake: Snake, snakes: list[Snake] = []) -> list[Snake]:
        for snake in snakes:
            if(snake.head == new_snake.head):
                raise NewHeadSnakeEqualHeadSnakeError(snake.head, snake.finish, new_snake.head)

            if(snake.tail == new_snake.head):
                raise NewHeadSnakeChainTailSnakeError(snake.head, snake.finish, new_snake.head)

            if(snake.head == new_snake.tail):
                raise NewTailSnakeChainHeadSnakeError(snake.head, snake.tail, new_snake.tail)

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

