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


@validate_args
def test(a):
    print('Success!')

print(test())
print(test(1, 2, 3))
print(test('100'))
print(test(-100))
print(test(100)) #None вывелось потому что пытаемся вывести на экран функцию, ничего не возвращающую