# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/6/ALDS1_6_A


def counting_sort(A, k):
    B = [0]*(len(A)+1)  # 1-based index
    C = [0]*(k+1)

    # CのインデックスCi=0..kはその数自身の出現回数を値に持つ
    # counter
    for a in A:
        C[a] += 1

    # accumulate
    tmp = 0
    for i in range(len(C)):
        tmp += C[i]
        C[i] = tmp

    for i in range(len(A))[::-1]:
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1

    return B[1:]


def main():
    n = int(input())
    A = list(map(int, input().split()))
    k = max(A)

    res = counting_sort(A, k)
    print(*res)


if __name__ == "__main__":
    main()
