from _typeshed import NoneType
from sys import platform
from board import Board
from player import Player
from random import randint

class Game:

    def __init__(self, board: Board, player: Player) -> None:
        self.board = board
        self.player = player

    def move_player(self, step: int) -> None:
        self.player.position += step

    def move_player_to(self, position: int) -> None:
        self.player.position = position

    def toss_dice(self) -> int:
        return randint(1, 6)

    def is_over(self) -> bool:
        return self.player.position >= self.board.finish_line
    
    def play(self, steps: list[int]) -> None:
        self.player.position = self.board.start_line

        print("Game start")

        while True:
            command = input("Continue(Y/N)?: ")
            
            if(command == "N"):
                return

            step = self.toss_dice()
            self.move_player(step)

            print(f"Go to {self.player.position}")

            ladder = self.board.get_ladder_on_position_by_start_ladder(self.player.position)
            snake = self.board.get_snake_on_position_by_head_snake(self.player.position)

            if(ladder):
                self.move_player_to(ladder.finish)

                print(f"Take ladder to {self.player.position}")

            elif(snake):
                self.move_player_to(snake.tail)

                print(f"Take snake to {self.player.position}")

            if(self.is_over()):
                print("You win!")
                
                return

    # For testing and checking snake and ladder
    def show_snake(self) -> None:
        self.board.show_snake()

    def show_ladder(self) -> None:
        self.board.show_ladder()
