def tests():
    print('---------Тесты из условия---------')
    print(find_coordinates(0))
    print(find_coordinates(1))
    print(find_coordinates(2))
    print(find_coordinates(14))
    print('\n---------Расширенные тесты---------')
    for i in range(0, 25):
        print(i, find_coordinates(i))


def last_square_point(square_num):
    c = 3
    sum = 0
    for i in range(0, square_num):
        sum += c
        c += 2
    return sum


def square_number(n):
    i = 3
    cnt = 0
    while n > 0:
        n -= i
        i += 2
        cnt += 1
    return cnt

def find_coordinates(step_count):
    x = 0
    y = 0
    last_point = last_square_point(square_number(step_count))
    first_point = last_point - 2 * square_number(step_count)
    mid = (last_point + first_point) / 2

    if square_number(step_count) % 2 == 0:
        if step_count > mid:
            y = square_number(step_count) / 2
            x = (-square_number(step_count) / 2) + last_point - step_count

        else:
            x = square_number(step_count) / 2
            y = (-square_number(step_count) / 2) + step_count - first_point

    else:
        if step_count > mid:
            y = -square_number(step_count) // 2
            x = (-square_number(step_count) // 2) + step_count - mid
        else:
            x = -square_number(step_count) // 2
            y = (square_number(step_count) // 2) - step_count + first_point
    return (int(x), int(y))


n = int(input())
print(*find_coordinates(n))
#tests()
# Для проверки просто раскомментируйте верхнюю строку

