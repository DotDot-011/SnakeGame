# create coordinate for snake and ladder 
# change play() in class game
# change checking board condition 
from board import Board
from game import Game
from player import Player
from error import *

file = open("input.txt", 'r')
lines = file.readlines()
file.close()

def create_coordinate_from_str(string: str) -> tuple(int, int):
    parameters = string.split("\n")[0].split()
    start = parameters[0]
    finish = parameters[1]
    
    return (start, finish)

def list_ladder_coordinate() -> list[tuple(int, int)]:
    file = open("ladderconfig.txt", 'r')
    lines = file.readlines()
    file.close()

    return list(map(lambda line: create_coordinate_from_str(line), lines))

def list_snake_coordinate() -> list[tuple(int, int)]:
    file = open("snakeconfig.txt", 'r')
    lines = file.readlines()
    file.close()

    return list(map(lambda line: create_coordinate_from_str(line), lines))

for line in lines:
    words = line.split("\n")[0].split()
    command = words[0]
    parameters = words[1:]

    if(command == "create_game"):
        board_size = int(parameters[0])
        finish_line = int(parameters[1])
        ladder_coordinates = list_ladder_coordinate()
        snake_coordinates = list_snake_coordinate()
        
        try:
            board = Board(board_size, finish_line, ladder_coordinates, snake_coordinates)
            player = Player(position = board.start_line)
            game = Game(board, player)

            print(f"Created game board_size {board_size}")
        
        except Error as Er:
            print(Er.message)

    elif(command == "play"):
        game.play()

    # For testing and checking snake and ladder
    elif(command == "show_ladder"):
        game.show_ladder()

    elif(command == "show_snake"):
        game.show_snake()
