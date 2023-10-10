desk = []
temp = list(input())
desk.append(temp)
for i in range(len(temp) - 1):
    a = list(input())
    desk.append(a)


#Главная диагональ
if len(set(list(desk[i][i] for i in range(len(desk))))) == 1 and desk[0][0] != '_':
    print(desk[0][0])
    exit()


#Побочная диагональ
tempArr = list(desk[i][len(desk) - 1 - i] for i in range(len(desk)))
if len(set(tempArr)) == 1 and not '_' in tempArr:
    print(tempArr[0])
    exit()

for i in range(len(desk)):
    #Горизонтали
    if len(set(desk[i])) == 1 and desk[i][0] != '_':
        print(desk[i])
        exit()

    #Вертикали
    tempArr = list(desk[j][i] for j in range(len(desk)))
    if len(set(tempArr)) == 1 and not '_' in tempArr:
        print(tempArr[0])
        exit()

print('Ничья')