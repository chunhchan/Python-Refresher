# fib.py

import time
from functools import lru_cache
import matplotlib.pyplot as plt


def timer(func):
    timings = {}

    def wrapper(n: int) -> int:
        start = time.perf_counter()
        result = func(n)
        elapsed = time.perf_counter() - start

        print(f"Finished in {elapsed:.8f}s: f({n}) -> {result}")
        timings[n] = elapsed
        return result

    wrapper._timings = timings  # store timings on wrapper
    return wrapper


@lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)

    # timings are stored on the timer wrapper, which is fib.__wrapped__
    t = fib.__wrapped__._timings  # dict: n -> seconds

    xs = sorted(t.keys())
    ys = [t[n] for n in xs]

    plt.figure()
    plt.plot(xs, ys)
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Fibonacci timing (with lru_cache + timer)")
    plt.tight_layout()
    plt.savefig("fib.png", dpi=200)
    plt.close()
