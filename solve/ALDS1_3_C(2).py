# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_C
import re
from collections import deque
from sys import stdin


def main():
    stdin.readline()
    commands = re.split(r'\n', stdin.read())[:-1]

    dll = deque()

    # commands: insert x, delete x, deleteFirst, deleteLast
    for c in commands:
        try:
            if c[0] == "i":
                dll.appendleft(c[7:])
            elif c[6] == "F":
                dll.popleft()
            elif c[6] == "L":
                dll.pop()
            else:
                dll.remove(c[7:])
        except Exception:
            pass

    print(*dll)


if __name__ == "__main__":
    main()
