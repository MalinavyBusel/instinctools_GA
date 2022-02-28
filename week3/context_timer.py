from time import perf_counter


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = perf_counter()


if __name__ == '__main__':
    with Timer() as timer:
        a = 9**8**7

    print(timer())
