s = input()
index = 0
for i in range(0, len(s)):
    if s[i] == ',':
        index = i

s, i = s[:index], s[index+1:]

cnt = 0
for x in s:
    if i == x:
        cnt += 1
        continue
    print(cnt)
    break
