a = input()
res = ''

for i in a:
    if i.isdigit() or i == '+':
        res += i
print(res)
