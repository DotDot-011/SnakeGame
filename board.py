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

    def check_board_size_more_than_zero(self, board_size: int) -> None:
        if(not(board_size > 0)):
            raise BoardSizeLessThanOneError(board_size)

    def check_finish_line_less_than_or_equal_board_size(self, finish_line: int, board_size: int) -> None:
        if(not(finish_line <= board_size)):
            raise FinishLineMoreThanBoardSizeError(finish_line, board_size)

    def check_finish_line_more_than_zero(self, finish_line: int) -> None:
        if(not(finish_line > 0)):
            raise FinishLineLessThanOneError(finish_line)

    def check_finish_line_not_start_line(self, finish_line: int, start_line: int) -> None:
        if(not(finish_line != start_line)):
            raise FinishLineEqualStartError(finish_line)

    def check_create_condition(self, board_size: int, finish_line: int, start_line: int) -> None:
        self.check_board_size_more_than_zero(board_size)
        self.check_finish_line_less_than_or_equal_board_size(finish_line)
        self.check_finish_line_more_than_zero(finish_line, board_size)
        self.check_finish_line_not_start_line(finish_line, start_line)

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

    def check_start_ladder_chain_start_ladder(self, first_ladder: Ladder, second_ladder: Ladder) -> None:
        if(first_ladder.start == second_ladder.start):
            raise NewStartLadderEqualStartLadderError(first_ladder.start, first_ladder.finish, second_ladder.start)

    def check_finish_ladder_chain_start_ladder(self, first_ladder: Ladder, second_ladder: Ladder) -> None:
        if(first_ladder.finish == second_ladder.start):
            raise NewStartLadderChainFinishLadderError(first_ladder.start, first_ladder.finish, second_ladder.start)

    def check_start_ladder_chain_finish_ladder(self, first_ladder: Ladder, second_ladder: Ladder) -> None:
        if(first_ladder.start == second_ladder.finish):
            raise NewFinishLadderChainStartLadderError(first_ladder.start, first_ladder.finish, second_ladder.start)

    def check_head_snake_chain_start_ladder(self, snake: Snake, ladder: Ladder) -> None:
        if(snake.head == ladder.start):
            raise NewStartLadderEqualHeadSnakeError(snake.head, snake.tail, ladder.start)
        
    def check_tail_snake_chain_start_ladder(self, snake: Snake, ladder: Ladder) -> None:
        if(snake.tail == ladder.start):
            raise NewStartLadderChainTailSnakeError(snake.head, snake.tail, ladder.start)

    def check_head_snake_chain_finish_ladder(self, snake: Snake, ladder: Ladder) -> None:
        if(snake.head == ladder.finish):
            raise NewFinishLadderChainHeadSnakeError(snake.head, snake.tail, ladder.finish)

    def check_start_ladder_chain_head_snake(self, ladder: Ladder, snake: Snake) -> None:
        if(ladder.start == snake.head):
            raise NewHeadSnakeEqualStartLadderError(ladder.start, ladder.finish, snake.head)

    def check_finish_ladder_chain_head_snake(self, ladder: Ladder, snake: Snake) -> None:
        if(ladder.finish == snake.head):
            raise NewHeadSnakeChainFinishLadderError(ladder.start, ladder.finish, snake.head)

    def check_start_ladder_chain_tail_snake(self, ladder: Ladder, snake: Snake) -> None:
        if(ladder.start == snake.tail):
            raise NewTailSnakeChainStartLadderError(ladder.start, ladder.finish, snake.tail)

    def check_head_snake_chain_head_snake(self, first_snake: Snake, second_snake: Snake) -> None:
        if(first_snake.head == second_snake.head):
            raise NewHeadSnakeEqualHeadSnakeError(first_snake.head, first_snake.tail, second_snake.head)

    def check_tail_snake_chain_head_snake(self, first_snake: Snake, second_snake: Snake) -> None:
        if(first_snake.tail == second_snake.head):
            raise NewHeadSnakeChainTailSnakeError(first_snake.head, first_snake.tail, second_snake.head)

    def check_head_snake_chain_tail_snake(self, first_snake: Snake, second_snake: Snake) -> None:
            if(first_snake.head == second_snake.tail):
                raise NewTailSnakeChainHeadSnakeError(first_snake.head, first_snake.tail, second_snake.tail)

    def check_chaining_ladder_with_ladder(self, new_ladder: Ladder, ladders: list[Ladder] = []) -> None:
        for ladder in ladders:
            self.check_start_ladder_chain_start_ladder(ladder, new_ladder)
            self.check_finish_ladder_chain_start_ladder(ladder, new_ladder)
            self.check_start_ladder_chain_finish_ladder(ladder, new_ladder)

    def check_chaining_snake_with_ladder(self, new_ladder: Ladder, snakes: list[Snake] = []) -> None:
        for snake in snakes:
            self.check_head_snake_chain_start_ladder(snake, new_ladder)
            self.check_tail_snake_chain_start_ladder(snake, new_ladder)
            self.check_head_snake_chain_finish_ladder(snake, new_ladder)

    def check_chaining_ladder_with_snake(self, new_snake: Snake, ladders: list[Ladder] = []) -> list[Ladder]:
        for ladder in ladders:
            self.check_start_ladder_chain_head_snake(ladder, new_snake)
            self.check_finish_ladder_chain_head_snake(ladder, new_snake)
            self.check_start_ladder_chain_tail_snake(ladder, new_snake)
          
    def check_chaining_snake_with_snake(self, new_snake: Snake, snakes: list[Snake] = []) -> list[Snake]:
        for snake in snakes:
            self.check_head_snake_chain_head_snake(snake, new_snake)
            self.check_tail_snake_chain_head_snake(snake, new_snake)
            self.check_head_snake_chain_tail_snake(snake, new_snake)

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

