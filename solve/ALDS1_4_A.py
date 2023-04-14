# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_A

def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    count = 0
    for i in range(q):
        for j in range(n):
            if S[j] == T[i]:
                count += 1
                break
    print(count)


if __name__ == "__main__":
    main()
