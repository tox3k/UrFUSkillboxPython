class Node:

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        a = self.start
        if self.end is self.start:
            self.start = None
            self.end = None
            return a
        self.start = self.start.nref

        return a.data

    def push(self, val):
        if self.start is None:
            self.start = Node(data=val)
            self.end = self.start

        else:
            a = Node(data=val)
            a.pref = self.end
            a.pref.nref = a
            self.end = a

    def insert(self, n, val):
        if n == 0:
            a = Node(data=val)
            a.nref = self.start
            self.start = a

        else:
            a = self.start
            for i in range(n):
                a = a.nref
            new_node = Node(data=val)

            if a is None:
                new_node.pref = a
                self.end.nref = new_node
                self.end = new_node
            else:
                a.pref.nref = new_node
                a.pref = new_node
                new_node.nref = a
                new_node.pref = a.pref

    def print(self):
        a = self.start
        while a is not None:
            print(a.data)
            a = a.nref

q = Queue()
q.push(1)
q.push(2)
q.insert(1, 3)
q.print()