from error import CannotCreateSnake

class Snake:

    # TODO: change name finish_line -> board_size
    def __init__(self, head: int, tail: int, finish_line: int) -> None:
        if(self.can_create(head, tail, finish_line)):
            raise(CannotCreateSnake(f"Can not create snake with head: {head}, tail: {tail}"))
  
        self.head = head
        self.tail = tail

    def can_create(self, head: int, tail: int, finish_line: int) -> bool:
        # TODO: raise error for each condition of created failure
        if(head <= tail):
            return False

        if(tail < 1):
            return False

        if(head >= finish_line):
            return False

        return True
