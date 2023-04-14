# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_C

import itertools


class Dictionary:
    def __init__(self):
        self.m = 1046527
        self.hash = [None]*self.m

    def get_char(self, ch):
        if ch == 'A':
            return 1
        elif ch == "C":
            return 2
        elif ch == "G":
            return 3
        elif ch == "T":
            return 4

    def get_key(self, s):
        sum = 0
        p = 1
        for c in s:
            sum += p*self.get_char(c)
            p *= 5
        return sum

    def h1(self, key):
        return key % self.m

    def h2(self, key):
        return 1+(key % (self.m-1))

    def h(self, key, i):
        return (self.h1(key)+i*self.h2(key)) % self.m

    def insert(self, s):
        key = self.get_key(s)
        for i in itertools.count():
            h_idx = self.h(key, i)
            hash_s = self.hash[h_idx]
            if hash_s is None:
                self.hash[h_idx] = s
                return h_idx
            elif hash_s == s:
                return False

    def find(self, s):
        key = self.get_key(s)
        for i in itertools.count():
            h_idx = self.h(key, i)
            hash_s = self.hash[h_idx]
            if hash_s == s:
                return True
            elif hash_s is None or i >= self.m:
                return False


def main():
    n = int(input())
    orders = [input().split() for _ in range(n)]

    d = Dictionary()
    for (o, val) in orders:
        if o == "insert":
            d.insert(val)
        else:
            print('yes' if d.find(val) else 'no')


if __name__ == "__main__":
    import timeit
    t = timeit.timeit(lambda: main(), number=1)
    print(f'{t:e}')
    # main()
