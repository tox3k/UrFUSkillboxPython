s = input()
index = 0
for i in range(0, len(s)):
    if s[i] == ',' and s[i+1] == ' ':
        index = i

a, b = int(s[:index]), int(s[index+2:])
if b != 0:
    print(a % b)
