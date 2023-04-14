# Program 6.1:nの階乗を計算する再帰関数

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(f"{factorial(10):,}")
