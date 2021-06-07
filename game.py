from board import Board
from player import Player
from dice import Dice


class Game:

    def __init__(self, board: Board, dice: Dice, players: list[Player]) -> None:
        self.board = board
        self.dice = dice
        self.players = players

    def move_player(self, player: Player, step: int) -> None:
        player.position += step

    def move_player_to(self, player: Player, position: int) -> None:
        player.position = position

    def is_player_win(self, player: Player) -> bool:
        return player.position >= self.board.finish_line

    def is_continue(self) -> bool:
        while True:
            command = input("Continue(Y/N)?: ")
            
            if(command == "N" or command == "n"):
                return False
            
            if(command == "Y" or command == "y"):
                return True
    
    def move_action(self, player: Player) -> None:
        step = self.dice.toss()

        self.move_player(player, step)
        
        ladder = self.board.get_ladder_by_start_on_position(player.position)

        if(ladder):
            self.move_player_to(player, ladder.finish)

            print(f"{player.name} take ladder to {player.position}")

        snake = self.board.get_snake_by_head_on_position(player.position)

        if(snake):
            self.move_player_to(player, snake.tail)

            print(f"{player.name} take snake to {player.position}")

    def play(self) -> None:
        is_end = False

        print("Game start")

        while not is_end:
            for player in self.players:
                self.move_action(player)

                print(f"{player.name} {player.position}")

                if(self.is_player_win(player)):
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

