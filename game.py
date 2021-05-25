from board import Board
from player import Player

class Game:

    def __init__(self, finish_line: int) -> None:
        # TODO: board ต้องสามารถรับ list ของ ladder และ snake เริ่มต้น เพื่อสร้าง board ที่พร้อมเล่นได้หลังสร้างเสร็จ
        self.board = Board(finish_line)

    def add_ladder(self, start: int, finish: int) -> None:
        self.board.add_ladder(start, finish)

    def add_snake(self, head: int, tail: int) -> None:
        self.board.add_snake(head, tail)

    def move_player(self, step: int) -> None:
        self.player.position += step

    def move_player_to(self, position: int) -> None:
        self.player.position = position

    def is_over(self) -> bool:
        if(self.player.position < self.board.finish_line):
            return False
        
        return True
    
    def play(self, steps: list[int]) -> str:
        self.player = Player(position = 1)

        print("Game start")

        for step in steps:
            self.move_player(step)

            print(f"Go to {self.player.position}")

            ladder = self.board.get_ladder_on_position(self.player.position)
            snake = self.board.get_snake_on_position(self.player.position)

            if(ladder):
                self.move_player_to(ladder.finish)

                print(f"Take ladder to {self.player.position}")

            elif(snake):
                self.move_player_to(snake.tail)

                print(f"Take snake to {self.player.position}")

            if(self.is_over()):
                return "You win!"
        
        return f"You are on the number {self.player.position}"

    # TODO: change comment -> For testing and checking snake and ladder
    # For check snake and ladder
    def show_snake(self) -> None:
        self.board.show_snake()

    def show_ladder(self) -> None:
        self.board.show_ladder()
