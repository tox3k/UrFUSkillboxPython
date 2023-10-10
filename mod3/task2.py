a = input()
print('Неверный ввод' if not a.isdigit() else ' '.join([bin(int(a)), oct(int(a)), hex(int(a))]))
