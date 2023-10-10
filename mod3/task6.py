a = input().split(' ')
print(*list(i[-1:] for i in a), sep='')