# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_D

count = 0


def insertion_sort(A, n, g):
    global count
    for i in range(g, n):
        j = i-g
        v = A[i]
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            count += 1
        A[j+g] = v
    return A


def generateG(n, m):
    G = [1]
    m -= 1
    for i in range(m):
        if 3*G[i]+1 > n:
            break
        G.append(3*G[i]+1)
    return G[::-1]


def shell_sort(A, n, G):
    global count
    result = A
    for g in G:
        result = insertion_sort(result, n, g)
    return result


def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    m = 100
    G = generateG(n, m)

    result = shell_sort(A, n, G)

    print(len(G))
    print(*G)
    print(count)
    for v in result:
        print(v)

    # print('m:', len(G))
    # print('G: ', G)
    # print('count:', count)
    # print('result:', result)


if __name__ == "__main__":
    main()
