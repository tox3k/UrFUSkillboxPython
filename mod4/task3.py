def euclid_alg(a, b):
    if a % b == 0:
        return b
    c = a % b
    a = b
    b = c
    return euclid_alg(a, b)


a, b = map(int, input().split(' '))
print(euclid_alg(a, b))
