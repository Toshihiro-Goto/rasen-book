# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_D
n = int(input())
r = [int(input()) for _ in range(n)]


minv = r[0]
maxv = -10**10
for i in range(1, n):
    maxv = max(maxv, r[i]-minv)
    minv = min(minv, r[i])


print(maxv)
