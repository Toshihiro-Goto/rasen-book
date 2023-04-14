# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, x):
        return self.stack.append(x)


def main():
    s = input().split()
    stack = Stack()

    def pop_twice():
        return stack.pop(), stack.pop()

    def calc(c):
        if c == "+":
            b, a = pop_twice()
            return a+b
        if c == "-":
            b, a = pop_twice()
            return a-b
        if c == "*":
            b, a = pop_twice()
            return a*b

    for c in s:
        if c.isdecimal():
            stack.push(int(c))
        else:
            stack.push(calc(c))

    print(stack.pop())


if __name__ == "__main__":
    main()
