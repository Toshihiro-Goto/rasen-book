# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_B

def binary_search(li, v):
    left = 0
    right = len(li)
    while left < right:
        mid = (left+right)//2
        if li[mid] == v:
            return True
        elif li[mid] < v:
            left = mid+1
        else:
            right = mid
    return False


def main():
    _ = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    count = 0
    for i in range(q):
        if binary_search(S, T[i]):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
