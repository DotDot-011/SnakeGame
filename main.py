from board import Board
from game import Game
from dice import Dice
from player import Player
from error import *


def create_coordinate_from_str(string: str) -> tuple[int, int]:
    parameters = string.split("\n")[0].split()
    start = int(parameters[0])
    finish = int(parameters[1])
    
    return (start, finish)


def list_ladder_coordinate() -> list[tuple[int, int]]:
    file = open("ladderconfig.txt", 'r')
    lines = file.readlines()
    file.close()

    return list(map(lambda line: create_coordinate_from_str(line), lines))


def list_snake_coordinate() -> list[tuple[int, int]]:
    file = open("snakeconfig.txt", 'r')
    lines = file.readlines()
    file.close()

    return list(map(lambda line: create_coordinate_from_str(line), lines))

def main():
    board_size = 100
    finish_line = 100
    start_line = 1
    ladder_coordinates = list_ladder_coordinate()
    snake_coordinates = list_snake_coordinate()
    
    try:
        board = Board(board_size, finish_line, ladder_coordinates, snake_coordinates, start_line)
        dice = Dice(6)
        game = Game(board, [Player(player_name = "Dog", position = start_line)])

        print(f"Created game success")
        game.play()
    
    except Error as Er:
        print(Er.message)

main()

