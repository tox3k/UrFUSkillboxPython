a = input()
res = ''
for i in range(len(a) - 1, -1, -1):
    if a[i] == '.':
        print(res)
        res = ''
        continue
    res = a[i] + res
    if i == 0:
        print(res)