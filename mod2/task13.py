a = input()
sum1 = 0
sum2 = 0
for i in range(0, len(a), 2):
    sum1 += int(a[i])

for i in range(1, len(a), 2):
    sum2 += int(a[i])
sum2 *= 3

if (sum1 + sum2) % 10 == 0:
    print('yes')
else:
    print('no')