a = list(map(int, input().split(' ')))
if len(set(a)) == 1:
    print('Все числа равны')

elif len(set(a)) == 2:
    print('Есть равные и неравные числа')

else:
    print('Все числа разные')