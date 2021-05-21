from error import CannotCreateLadder

class Ladder:

    def __init__(self, start: int, finish: int, finish_line: int) -> None:
        if(not self.can_create(start, finish)):
            raise CannotCreateLadder(f"Can not create ladder with start: {start}, finish: {finish}")
        
        self.start = start
        self.finish = finish

    def can_create(self, start: int, finish: int, finish_line: int) -> bool:
        if(start >= finish):
            return False

        if(start < 2):
            return False

        if(finish > finish_line):
            return False

        return True
