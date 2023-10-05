def get_bin_representation(num):
    res = ''
    while num > 0:
        res += str(num % 2)
        num //= 2
    return res[::-1]


def get_oct_representation(num):
    res = ''
    while num > 0:
        res += str(num % 8)
        num //= 8
    return res[::-1]


def get_hex_representation(num):
    res = ''
    while num > 0:
        ost = num % 16
        if ost < 10:
            res += str(ost)
        elif ost == 10:
            res += 'A'
        elif ost == 11:
            res += 'B'
        elif ost == 12:
            res += 'C'
        elif ost == 13:
            res += 'D'
        elif ost == 14:
            res += 'E'
        elif ost == 15:
            res += 'F'

        num //= 16
    return res[::-1]


a = int(input())
print(get_bin_representation(a), get_oct_representation(a), get_hex_representation(a))
