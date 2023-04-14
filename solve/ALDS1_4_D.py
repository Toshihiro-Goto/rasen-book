# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_D


def binary_search(length, v, func):
    left = 0
    right = length
    while right - left > 1:
        mid = (left+right)//2
        if func(mid) >= v:
            right = mid
        else:
            left = mid
    return right


def main():
    n, k = map(int, input().split())
    W = [int(input()) for _ in range(n)]

    def load_into_track(p):
        i = 0
        for _ in range(k):
            s = 0
            while s + W[i] <= p:
                s += W[i]
                i += 1
                if i == n:
                    return n
        return i

    max_n = 10**5
    max_w = 10**4
    p = binary_search(max_n*max_w, n, load_into_track)
    print(p)


if __name__ == "__main__":
    main()
