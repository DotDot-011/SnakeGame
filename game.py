from board import Board
from player import Player

class Game:

    def __init__(self, finish_line: int) -> None:
        self.board = Board(finish_line)

    def add_ladder(self, start: int, finish: int) -> None:
        self.board.add_ladder(start, finish)

    def add_snake(self, head: int, tail: int) -> None:
        self.board.add_snake(head, tail)

    def move(self, step: int) -> None:
        self.player.position += step

    def move_to(self, position: int) -> None:
        self.player.position = position

    def is_win(self) -> bool:
        if(self.player.position < self.board.finish_line):
            return False
        
        return True
    
    def play(self, steps: list[int]) -> str:
        self.player = Player(position = 1)

        print("Game start")

        for step in steps:
            self.move(step)

            print(f"Go to {self.player.position}")

            ladder = self.board.get_ladder_on_position(self.player.position)
            snake = self.board.get_snake_on_position(self.player.position)

            if(ladder):
                self.move_to(ladder.finish)

                print(f"Take ladder to {self.player.position}")

            elif(snake):
                self.move_to(snake.tail)

                print(f"Take snake to {self.player.position}")

            if(self.is_win()):
                return "You win!"
        
        return f"You are on the number {self.player.position}"

    # For check snake and ladder
    def show_snake(self) -> None:
        self.board.show_snake()

    def show_ladder(self) -> None:
        self.board.show_ladder()
