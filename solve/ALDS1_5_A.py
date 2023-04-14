# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/5/ALDS1_5_A

from functools import lru_cache


def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    m = list(map(int, input().split()))

    @lru_cache(maxsize=None)
    def solve(i, m):
        if m == 0:
            return True
        if i >= n:
            return False

        a = solve(i+1, m-A[i])  # i番目の要素を使う場合
        b = solve(i+1, m)   # i番目の要素を使わない場合
        return a or b

    ress = [solve(0, mi) for mi in m]
    for res in ress:
        ans = "yes" if res else "no"
        print(ans)


if __name__ == "__main__":
    main()
