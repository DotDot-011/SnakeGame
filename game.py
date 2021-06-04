from board import Board
from player import Player
from dice import Dice
from random import randint


class Game:

    def __init__(self, board: Board, dice: Dice, players: list[Player]) -> None:
        self.board = board
        self.dice = dice
        self.players = players

    def move_player(self, player: Player, step: int) -> None:
        player.position += step

    def move_player_to(self, player: Player, position: int) -> None:
        player.position = position

    def toss_dice(self) -> int:
        return randint(1, 6)

    def player_win(self, player: Player) -> bool:
        return player.position >= self.board.finish_line

    def is_continue(self) -> bool:
        while True:
            command = input("Continue(Y/N)?: ")
            
            if(command == "N" or command == "n"):
                return False
            
            if(command == "Y" or command == "y"):
                return True
    
    def play(self) -> None:
        is_end = False

        print("Game start")

        while not is_end:
            for player in self.players:
                step = self.dice.toss()

                print(f"{player.name} toss dice and get {step}")

                self.move_player(player, step)

                print(f"{player.name} go to {player.position}")

                ladder = self.board.get_ladder_by_start_on_position(player.position)
                snake = self.board.get_snake_by_head_on_position(player.position)

                if(ladder):
                    self.move_player_to(player, ladder.finish)

                    print(f"{player.name} take ladder to {player.position}")

                elif(snake):
                    self.move_player_to(snake.tail)

                    print(f"{player.name} take snake to {player.position}")

                if(self.player_win(player)):
                    print(f"{player.name} win!")
                    
                    is_end = True
                    
                    break

            if(not self.is_continue()):
                is_end = True

    # For testing and checking snake and ladder
    def show_snake(self) -> None:
        self.board.show_snake()

    def show_ladder(self) -> None:
        self.board.show_ladder()

