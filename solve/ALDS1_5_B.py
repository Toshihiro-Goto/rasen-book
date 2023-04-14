# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_B

count = 0


def merge(A, l, m, r):
    global count
    banpei = 10**10
    L = A[l:m]+[banpei]
    R = A[m:r]+[banpei]
    i = 0
    j = 0
    for k in range(l, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            count += 1
        else:
            A[k] = R[j]
            j += 1
            count += 1


def merge_sort(A, l, r):
    if r-l > 1:
        m = (l+r)//2
        merge_sort(A, l, m)
        merge_sort(A, m, r)
        merge(A, l, m, r)


def main():
    n = int(input())
    A = list(map(int, input().split()))

    merge_sort(A, 0, n)

    print(*A)
    print(count)


if __name__ == "__main__":
    main()
