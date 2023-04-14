import re
from sys import stdin


def Node(key): return {'prev': None, 'key': key, 'next': None}


class DoublyLinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.nil['prev'] = self.nil
        self.nil['next'] = self.nil
        self.len = 0
        self.list_max = 10**6

    def insert(self, key):
        insert_node = Node(key)
        next_node = self.nil['next']
        prev_node = self.nil

        insert_node['next'] = next_node
        insert_node['prev'] = prev_node

        next_node['prev'] = insert_node
        prev_node['next'] = insert_node
        self.len += 1

    def search(self, key):
        node = self.nil['next']
        for _ in range(len(self)):
            if node['key'][7:] == key[7:] or node is self.nil:
                break
            node = node['next']
        return node

    def delete_key(self, key):
        node = self.search(key)
        self.delete_node(node)

    def delete_node(self, node):
        if node is self.nil:
            return
        next_node = node['next']
        prev_node = node['prev']
        next_node['prev'] = prev_node
        prev_node['next'] = next_node
        self.len -= 1

    def delete_first(self):
        self.delete_node(self.nil['next'])

    def delete_last(self):
        self.delete_node(self.nil['prev'])

    def print(self):
        node = self.nil['next']
        for _ in range(self.list_max):
            if node['next'] is self.nil:
                print(node['key'][7:])
                break
            print(node['key'][7:], end=' ')
            node = node['next']

    def __len__(self):
        return self.len


def main():
    n = int(stdin.readline()[:-1])
    commands = re.split(r'\n', stdin.read())[:-1]

    dll = DoublyLinkedList()

    # commands: insert x, delete x, deleteFirst, deleteLast
    for c in commands:
        if c[0] == "i":
            dll.insert(c)
        elif c[6] == "F":
            dll.delete_first()
        elif c[6] == "L":
            dll.delete_last()
        else:
            dll.delete_key(c)

    dll.print()


if __name__ == "__main__":
    main()
