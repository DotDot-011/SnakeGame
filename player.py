class Player:
    
    def __init__(self, position: int) -> None:
        self.position = position

    def move(self, step: int) -> None:
        self.position += step

    def move_to(self, target: int) -> None:
        self.position = target