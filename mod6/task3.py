def get_sum(num, pow):
    res = 0
    s = str(num)
    for i in s:
        res += int(i)**pow
    return res


def get_armstrong_numbers():
    i = 10
    while True:
        i += 1
        if get_sum(i, len(str(i))) == i:
            yield i


arm = get_armstrong_numbers()


def get_armstrong_numbers():
    return next(arm)

for i in range(100):
    print(get_armstrong_numbers())
