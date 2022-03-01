from time import perf_counter
from typing import Optional, Type
from types import TracebackType


class Timer:
    def __init__(self):
        self.total_time = float('nan')

    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]):
        self.end = perf_counter()
        self.total_time = self.end - self.start


if __name__ == '__main__':
    my_timer = Timer()
    with my_timer as timer:
        a = 9**8**7
    print(my_timer.total_time)
