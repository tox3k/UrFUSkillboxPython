import time
fib_res = dict()


def validate_args(func):
    def wrapped_func(*args):
        if len(args) < 1:
            return 'Not enough arguments'
        if len(args) > 1:
            return 'Too many arguments'
        if not isinstance(*args, int):
            return 'Wrong types'
        if args[0] < 0:
            return 'Negative argument'
        return func(*args)

    return wrapped_func

def memoize(func):
    def wrapped_func(*args):
        if fib_res.get(*args) is not None:
            return fib_res.get(*args)
        else:
            fib_res[args[0]] = func(*args)
            return fib_res.get(*args)

    return wrapped_func

def timer(func, currently_evaluating=set()):
    def wrapped_func(x):
        if func in currently_evaluating:
            return func(x)
        else:
            start_time = time.time_ns()
            currently_evaluating.add(func)
            try:
                value = func(x)
            finally:
                currently_evaluating.remove(func)
            end_time = time.time_ns()
            print('time taken: {time} nanoseconds'.format(time=end_time-start_time))
            return value
    return wrapped_func

@timer
@memoize
@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@timer
def bad_fibonacci(n):
    if n < 2:
        return n
    return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)

fibonacci(30)
bad_fibonacci(30)
