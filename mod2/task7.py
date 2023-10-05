def char_count(char, string):
    cnt = 0
    for i in string:
        if char == i:
            cnt += 1
    return cnt


a = input()
if char_count('0', a) == char_count('1', a):
    print('yes')
else:
    print('no')
