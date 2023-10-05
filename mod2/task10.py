a = input()

res = ''

for i in range(0, len(a)):
    if a[i] == ' ':
        res += a[i - 1]
res += a[-1:]

print(res)
