# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_B

n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(n):
    minj = i
    for j in range(i, n):
        if a[j] < a[minj]:
            minj = j
    a[i], a[minj] = a[minj], a[i]
    if minj != i:
        count += 1

print(*a)
print(count)
