import time
import traceback
fib_res = dict()
func_name = ''

def memoize(func):
    def wrapped_func(*args):
        if fib_res.get(*args) is not None:
            return fib_res.get(*args)
        else:
            fib_res[args[0]] = func(*args)
            return fib_res.get(*args)

    return wrapped_func

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def bad_fibonacci(n):
    if n < 2:
        return n
    return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


start = time.time_ns()

for i in range(20):
    fibonacci(i)

print(time.time_ns() - start)
start = time.time_ns()

for i in range(20):
    bad_fibonacci(i)

print(time.time_ns() - start)

#Добавил сравнение по времени чтоб вы поверили что всё работает