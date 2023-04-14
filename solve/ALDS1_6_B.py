# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/6/ALDS1_6_B

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def main():
    n = int(input())
    A = list(map(int, input().split()))
    res = partition(A, 0, n-1)
    for i in range(n):
        if i == res:
            A[i] = f"[{A[i]}]"
    print(*A)


if __name__ == "__main__":
    main()
