# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B

class CircularQueue:
    def __init__(self, length):
        self.max = length + 1
        self.queue = [0 for _ in range(self.max)]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == (self.tail + 1) % self.max

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError()
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.max

    def dequeue(self):
        if self.is_empty():
            raise IndexError()
        x = self.queue[self.head]
        self.head = (self.head + 1) % self.max
        return x


def main():
    n, q = map(int, input().split())

    def input_as_dict():
        a, b = input().split()
        return dict(name=a, time=int(b))

    ps = [input_as_dict() for _ in range(n)]

    queue = CircularQueue(n)
    for p in ps:
        queue.enqueue(p)

    current_time = 0
    while not queue.is_empty():
        p = queue.dequeue()
        result = p['time'] - q
        if result > 0:
            p['time'] = result
            queue.enqueue(p)
            current_time += q
        else:
            current_time += p['time']
            print(p['name'], current_time)


if __name__ == "__main__":
    main()
