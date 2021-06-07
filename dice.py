from random import randint
from error import DiceFaceLessThanOneError


class Dice():
    
    def __init__(self, face_count: int) -> None:
        self.check_create_condition(face_count)

        self.face_count = face_count

    def check_face_count_more_than_zero(face_count):
        if(not(face_count > 0)):
            raise DiceFaceLessThanOneError(face_count)

    def check_create_condition(self, face_count) -> None:
        self.check_face_count_more_than_zero(face_count)

    def toss(self) -> int:
        return randint(1, self.face_count)
