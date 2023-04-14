# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_A

n = int(input())
a = list(map(int, input().split()))

count = 0
flag = True
i = 0
while flag:
    flag = False
    for j in range(i+1, n)[::-1]:
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            flag = True
            count += 1
    i += 1

print(*a)
print(count)
