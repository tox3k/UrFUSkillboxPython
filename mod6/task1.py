class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)


    def get(self, index):
        if index < 0:
            raise Exception('IndexOutOfBounds')
        element = self.head
        for i in range(index):
            if element is None:
                raise Exception('IndexOutOfBounds')
            element = element.next
        return element.data

    def remove(self, index):
        if index < 0:
            raise Exception('IndexOutOfBounds')

        node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index - 1):
                if node.next is None:
                    raise Exception('IndexOutOfBounds')
                node = node.next
                if node.next is None:
                    raise Exception('IndexOutOfBounds')

        if node.next is not None:
            node.next = node.next.next

    def insert(self, index, value):
        if index < 0:
            raise Exception('IndexOutOfBounds')

        if index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            for i in range(index - 1):
                if node is None:
                    raise Exception('IndexOutOfBounds')
                node = node.next
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node

    def print(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


s = LinkedList()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print()
print('--------')
s.remove(2)
s.print()
print('--------')
s.insert(2, 100)
s.print()
print('--------')
print(s.get(2))
