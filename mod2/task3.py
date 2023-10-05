s = input()
index1 = 0
index2 = 0
flag = True

for i in range(0, len(s)):
    if s[i] == ' ' and flag:
        index1 = i
        flag = False

    if s[i] == ' ' and not flag:
        index2 = i

a, b, c = int(s[0:index1]), int(s[index1 + 1:index2]), int(s[index2:])

if a >= b >= c or c >= b >= a:
    print(b)
elif c >= a >= b or b >= a >= c:
    print(a)
elif b >= c >= a or a >= c >= b:
    print(a)
