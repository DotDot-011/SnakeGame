from typing import Optional
from ladder import Ladder
from snake import Snake
from error import *

class Board:
    
    def __init__(self, finish_line: int) -> None:
        self.finish_line = finish_line
        self.snakes = []
        self.ladders = []

    def can_add_ladder(self, new_ladder: Ladder) -> bool:
        if(new_ladder.start > new_ladder.finish):
            return False

        if(new_ladder.finish > self.finish_line):
            return False
        
        ladders = list(filter(lambda ladder: (ladder.start == new_ladder.start) 
        or (ladder.finish == new_ladder.start) 
        or (ladder.start == new_ladder.finish), self.ladders))
        snakes = list(filter(lambda snake: (snake.head == new_ladder.start) 
        or (snake.tail == new_ladder.start) 
        or (snake.head == new_ladder.finish), self.snakes))

        if(ladders or snakes):
            return False

        return True

    def can_add_snake(self, new_snake: Snake) -> bool:
        if(new_snake.head < new_snake.tail):
            return False
        
        if(new_snake.head >= self.finish_line):
            return False

        ladders = list(filter(lambda ladder: (ladder.start == new_snake.head) 
        or (ladder.finish == new_snake.head) 
        or (ladder.start == new_snake.tail), self.ladders))
        snakes = list(filter(lambda snake: (snake.head == new_snake.head) 
        or (snake.tail == new_snake.head) 
        or (snake.head == new_snake.tail), self.snakes))

        if(ladders or snakes):
            return False
        
        return True

    def add_ladder(self, start: int, finish: int) -> None:
        ladder = Ladder(start, finish)
        
        if(not self.can_add_ladder(ladder)):
            raise CannotAddLadder(f"Ladder with start: {ladder.start}, finish: {ladder.finish} cannot be added.")

        self.ladders.append(ladder)

    def add_snake(self, head: int, tail: int) -> None:
        snake = Snake(head, tail)

        if(not self.can_add_snake(snake)):
            raise CannotAddSnake(f"Snake with head: {snake.head}, tail: {snake.tail} cannot be added.")

        self.snakes.append(snake)

    def get_ladder_on_position(self, position: int) -> Optional[Ladder]:
        ladders = list(filter(lambda ladder: ladder.start == position, self.ladders))

        if(not ladders):
            return None

        return ladders[0]

    def get_snake_on_position(self, position: int) -> Optional[Snake]:
        snakes = list(filter(lambda snake: snake.head == position, self.snakes))

        if(not snakes):
            return None

        return snakes[0]

    # For check snake and ladder
    def show_snake(self) -> None:
        print("List of snake:")

        for snake in self.snakes:
            print(f"snake with head: {snake.head}, tail: {snake.tail}")

    def show_ladder(self) -> None:
        print("List of ladder:")

        for ladder in self.ladders:
            print(f"ladder with start: {ladder.start}, finish: {ladder.finish}")
