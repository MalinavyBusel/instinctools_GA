from time import perf_counter


class Timer:
    def __init__(self):
        self.total_time = 0.0

    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()
        self.total_time = self.end - self.start


if __name__ == '__main__':
    my_timer = Timer()
    with my_timer as timer:
        a = 9**8**7
    print(my_timer.total_time)