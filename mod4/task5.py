a = input()

d = dict()


for i in range(len(a)):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1

l = []
for tup in d.items():
    l.append((tup[1], tup[0]))

for i in sorted(l):
    print(i[1], i[0])