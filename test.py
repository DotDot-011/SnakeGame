from typing import IO


class error_test():
    
    def __init__(self) -> None:
        self.a = 10
        raise IOError()
        self.b = 15

try:
    cd = error_test()
    print(cd.a)
except IOError:
    print(cd.a)