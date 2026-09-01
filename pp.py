import time
from typing import Callable
def limit_call(limit: int):
    def wrapper(func: Callable):
        def inner(*args, **kwargs):
            nonlocal limit
            if limit == 0:
                print('лимит достигнут')
                return
            
            res = func(*args, **kwargs)
            limit -= 1
            return res
        return inner
    return wrapper

@limit_call(2)
def my_func(sleep_sec: int):
    time.sleep(sleep_sec)
    return 5

print(my_func(3))
print(my_func(3))
print(my_func(3))

