# Found on stackoverflow from user JBirdVegas
# https://stackoverflow.com/questions/51503672/decorator-for-timeit-timeit-method

from functools import wraps
from time import time
def time(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _time_it