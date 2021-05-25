# TODO: change Project name SnakeGame -> SnakeAndLadderGame
from game import Game
from error import *

file = open("input.txt", 'r')
lines = file.readlines()
file.close()

for line in lines:
    words = line.split("\n")[0].split()
    command = words[0]
    parameters = words[1:]

    if(command == "create_game"):
        # TODO: change name finish_line -> board_size
        finish_line = int(parameters[0])

        try:
            game = Game(finish_line)

            print(f"Created game with finish line {finish_line}")
        
        except Error as Er:
            print(Er.message)

    elif(command == "add_ladder"):
        start = int(parameters[0])
        finish = int(parameters[1])

        try:
            game.add_ladder(start, finish)

            print(f"Added ladder with start: {start}, finish: {finish}")

        except Error as Er:
            print(Er.message)

    elif(command == "add_snake"):
        head = int(parameters[0])
        tail = int(parameters[1])

        try:
            game.add_snake(head, tail)

            print(f"Added snake with head: {head}, tail: {tail}")

        except Error as Er:
            print(Er.message)

    # TODO: แยก funtion ระหว่าง play กับ เช็กว่า ชนะรึยัง ออกจากกัน
    elif(command == "play"):
        steps = list(map(lambda parameter: int(parameter), parameters))

        status = game.play(steps)
        
        print(status)

    # TODO: change comment -> For testing and checking snake and ladder
    # For check snake and ladder
    elif(command == "show_ladder"):
        game.show_ladder()

    elif(command == "show_snake"):
        game.show_snake()
