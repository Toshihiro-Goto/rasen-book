# Program 6.2: 最大値を求めるアルゴリズム

def find_maximum(A, l, r):
    m = (l+r)//2 # ()のつけ忘れに注意
    if r-l == 1:
        return A[l]
    else:
        a = find_maximum(A, l, m)
        b = find_maximum(A, m, r)
        x = max(a, b)
    return x


li = [67, 346, 234, 456, 234, 67245, 745, 63, 4565, 234, 5234, 5234, ]
l = 0
r = len(li)
print(find_maximum(li, l, r))
