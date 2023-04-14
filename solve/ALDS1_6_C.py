# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/6/ALDS1_6_C


def partition(A, p, r, key=lambda x: x):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if key(A[j]) <= key(x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def quick_sort(A, key):
    def _sort(A, p, r, key):
        if p < r:
            q = partition(A, p, r, key)
            _sort(A, p, q-1, key)
            _sort(A, q+1, r, key)
    A = A.copy()
    _sort(A, 0, len(A)-1, key)
    return A


def main():
    n = int(input())
    A = [input() for _ in range(n)]

    def get_card_num(x): return int(x[2:])
    quick_sorted_A = quick_sort(A, key=get_card_num)
    stable_sorted_A = sorted(A, key=get_card_num)

    is_stable_sorted = all(
        [a == b for a, b in zip(quick_sorted_A, stable_sorted_A)])

    print('Stable' if is_stable_sorted else 'Not stable')
    for a in quick_sorted_A:
        print(a)


if __name__ == "__main__":
    main()
