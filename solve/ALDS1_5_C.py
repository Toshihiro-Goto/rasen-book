# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_C


import math


def nth_div(p1, p2, nth, div_n):
    return (p1[0]+(p2[0]-p1[0]) * nth/div_n, p1[1]+(p2[1]-p1[1])*nth/div_n)


def rotate_60(p1, p2):
    cos = math.cos
    sin = math.sin
    PI = math.pi
    p1x, p1y = p1
    p2x, p2y = p2
    p3x = (p2x-p1x)*cos(PI/3)-(p2y-p1y)*sin(PI/3)+p1x
    p3y = (p2x-p1x)*sin(PI/3)+(p2y-p1y)*cos(PI/3)+p1y
    return (p1, (p3x, p3y))


def koch(p1, p2, n):
    if n == 0:
        return
    s = nth_div(p1, p2, 1, 3)
    t = nth_div(p1, p2, 2, 3)
    u = rotate_60(s, t)[1]

    koch(p1, s, n-1)
    print(*s)
    koch(s, u, n-1)
    print(*u)
    koch(u, t, n-1)
    print(*t)
    koch(t, p2, n-1)


def main():
    n = int(input())
    p1 = (0, 0)
    p2 = (100, 0)
    print(*p1)
    koch(p1, p2, n)
    print(*p2)


if __name__ == "__main__":
    main()
