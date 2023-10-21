a = input()
cnt = 0
d = dict()

for i in range(len(a)):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

for key, value in d.items():
    if value % 2 != 0:
        cnt += 1

if cnt <= 1:
    mid = None
    res = ''
    for k, v in d.items():
        if v > 1:
            res += k
        else:
            mid = k
    if mid is not None:
        print(res + mid + res[::-1])
    else:
        print(res + res[::-1])
else:
    print('Нельзя составить палиндром')