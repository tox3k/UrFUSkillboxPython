class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел


class Stack:

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        if self.end.pref is None:
            val = self.end.data
            self.end = None
            return val

        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        if self.end is None:
            self.end = Node(data=val)
        else:
            a = Node(data=val)
            a.pref = self.end
            self.end = a

    def print(self):
        a = self.end
        while a is not None:
            print(a.data)
            a = a.pref


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()

s.print()
