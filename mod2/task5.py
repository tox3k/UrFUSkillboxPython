s = input()
index = 0
for i in range(0, len(s)):
    if s[i] == ',':
        index = i

i, n = s[:index], int(s[index+1:])

alph = 'abcdefghijklmnopqrstuvwxyz'
print(alph[(alph.index(i) + n) % 26])