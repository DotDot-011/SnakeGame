from board import Board
from Error import *

file = open("input.txt", 'r')
lines = file.readlines()
file.close()

for line in lines:
    words = line.split("\n")[0].split()
    command = words[0]
    parameters = words[1:]

    if(command == "create_game"):
        finish_line = int(parameters[0])

        game = Board(finish_line)

        print(f"Create game with finish line {finish_line}")

    elif(command == "add_stair"):
        start = int(parameters[0])
        stop = int(parameters[1])

        try:
            game.add_stair(start, stop)

            print(f"Add stair with start: {start}, stop: {stop}")

        except Error as Er:
            print(Er.message)

    elif(command == "add_snake"):
        head = int(parameters[0])
        tail = int(parameters[1])

        try:
            game.add_snake(head, tail)

            print(f"Add snake with head: {head}, tail: {tail}")

        except Error as Er:
            print(Er.message)

    elif(command == "show_stair"):
        game.show_stair()

    elif(command == "show_snake"):
        game.show_snake()

    if(command == "play"):
        steps = list(map(lambda parameter: int(parameter), parameters))

        status = game.play(steps)
        
        print(f"Now you are {status}")