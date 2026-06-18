"""
Create a reusable function decorator named `@track_execution_time`. When added on top of any target
computational function, it wraps execution logic, monitors precision duration benchmarks, and automatically
logs performance diagnostic outputs.
Sample Input: @track_execution_time
def compute_squares(): ...
Expected Output: Console Log: 'Function compute_squares executed in 0.0412 seconds.'
"""

import time

def track_execution_time(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(
            f"Function {func.__name__} executed in "
            f"{end - start:.4f} seconds."
        )

        return result

    return wrapper


@track_execution_time
def compute_squares():

    total = []

    for i in range(100000):
        total.append(i * i)

    return total


compute_squares()