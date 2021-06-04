from random import randint
from error import DiceFaceLessThanOneError


class Dice():
    
    def __init__(self, face_count: int) -> None:
        self.face_count = face_count

    def check_create_condition(self, face_count) -> None:
        if(face_count < 1):
            raise DiceFaceLessThanOneError(face_count)

    def toss(self) -> int:
        return randint(1, self.face_count)
