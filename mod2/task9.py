s = input()

glas = 'аеёиоуыэюя'
sogl = 'йцкнгшщзхфвпрлджчсмтб'

glas_cnt = 0
sogl_cnt = 0

for i in s:
    if glas.find(i) > -1:
        glas_cnt += 1
    elif sogl.find(i) > 0:
        sogl_cnt += 1
print(glas_cnt, sogl_cnt)