class DoubleElement:
    def __init__(self, *lst):
        self.data = [*lst]
        self._current = 0

    def __next__(self):
        self._current += 2
        if self._current < len(self.data):
            if self._current == len(self.data) - 1 and len(self.data) % 2 != 0:
                return (self.data[self._current]),None
            else:
                return (self.data[self._current]), self.data[self._current + 1]

    def __iter__(self):
        for i in range(0, len(self.data), 2):
            a = self.data[i]
            if i == len(self.data) - 1 and len(self.data) % 2 != 0:
                b = None
            else:
                b = self.data[i + 1]
            yield (a, b)


dL = DoubleElement(1,2,3,4,5)
for pair in dL:
    print(pair)

print()
