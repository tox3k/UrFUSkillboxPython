a = input()
for i in range(0, len(a) - 2):
    if a[i] == ' ':
        continue
    if a[i + 1:].find(a[i]) > -1:
        print(True)
        exit()
print(False)
