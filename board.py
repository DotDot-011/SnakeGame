from typing import Optional, Union
from stair import Stair
from snake import Snake
from player import Player
from Error import *

class Board:
    
    def __init__(self, finish_line: int) -> None:
        self.finish_line = finish_line
        self.snakes = []
        self.stairs = []

    def can_add_stair(self, new_stair: Stair) -> bool:
        if(new_stair.start > new_stair.stop):
            return False

        if(new_stair.stop > self.finish_line):
            return False
        
        stairs = list(filter(lambda stair: (stair.start == new_stair.start) 
        or (stair.stop == new_stair.start) 
        or (stair.start == new_stair.stop), self.stairs))
        snakes = list(filter(lambda snake: (snake.head == new_stair.start) 
        or (snake.tail == new_stair.start) 
        or (snake.head == new_stair.stop), self.snakes))

        if(stairs or snakes):
            return False

        return True

    def can_add_snake(self, new_snake: Snake) -> bool:
        if(new_snake.head < new_snake.tail):
            return False
        
        if(new_snake.head > self.finish_line):
            return False

        stairs = list(filter(lambda stair: (stair.start == new_snake.head) 
        or (stair.stop == new_snake.head) 
        or (stair.start == new_snake.tail), self.stairs))
        snakes = list(filter(lambda snake: (snake.head == new_snake.head) 
        or (snake.tail == new_snake.head) 
        or (snake.head == new_snake.tail), self.snakes))

        if(stairs or snakes):
            return False
        
        return True

    def add_stair(self, start: int, stop: int) -> None:
        stair = Stair(start, stop)
        
        if(not self.can_add_stair(stair)):
            raise CannotAddStair(f"Stair with start: {stair.start}, stop: {stair.stop} cannot be added.")

        self.stairs.append(stair)

    def add_snake(self, head: int, tail: int) -> None:
        snake = Snake(head, tail)

        if(not self.can_add_snake(snake)):
            raise CannotAddSnake(f"Snake with head: {snake.head}, tail: {snake.tail} cannot be added.")

        self.snakes.append(snake)

    def get_stair_on_position(self, position: int) -> Optional[Stair]:
        stairs = list(filter(lambda stair: stair.start == position, self.stairs))

        if(not stairs):
            return None

        return stairs[0]

    def get_snake_on_position(self, position: int) -> Optional[Snake]:
        snakes = list(filter(lambda snake: snake.head == position, self.snakes))

        if(not snakes):
            return None

        return snakes[0]

    def is_win(self, player: Player) -> bool:
        if(player.position < self.finish_line):
            return False

        return True

    def play(self, steps: list[int]) -> Union[int, str]:
        self.player = Player(1)

        print("Game Start")

        for step in steps:
            self.player.move(step)

            print(f"go to {self.player.position}")

            stair = self.get_stair_on_position(self.player.position)
            snake = self.get_snake_on_position(self.player.position)

            if(stair):
                self.player.move_to(stair.stop)

                print(f"take stair from {stair.start} to {stair.stop}")

            elif(snake):
                self.player.move_to(snake.tail)

                print(f"take snake from {snake.head} to {snake.tail}")

            if(self.is_win(self.player)):
                return "win"
        
        return self.player.position

    def show_snake(self) -> None:
        print("List of snake:")

        for snake in self.snakes:
            print(f"snake with head: {snake.head}, tail: {snake.tail}")

    def show_stair(self) -> None:
        print("List of stair:")

        for stair in self.stairs:
            print(f"stair with start: {stair.start}, stop: {stair.stop}")