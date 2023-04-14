# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_C

def bubble_sort(c, n):
    flag = True
    while flag:
        flag = False
        for i in range(1, n)[::-1]:
            if c[i-1][1] > c[i][1]:
                c[i-1], c[i] = c[i], c[i-1]
                flag = True
    return c


def selection_sort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if c[j][1] < c[minj][1]:
                minj = j
        c[i], c[minj] = c[minj], c[i]
    return c


# def is_stable(unsorted, sorted):
#     n = len(unsorted)
#     for i in range(n):
#         for j in range(i, n):
#             for a in range(n):
#                 for b in range(a+1, n):
#                     if unsorted[i][1] == unsorted[j][1] \
#                             and unsorted[i] == sorted[b] \
#                             and unsorted[j] == sorted[a]:
#                         return False
#     return True


def is_stable2(stable_sorted, sorted):
    n = len(stable_sorted)
    for i in range(n):
        if stable_sorted[i] != sorted[i]:
            return False
    return True


def main():
    n = int(input())
    c = input().split()

    bubble_sorted = bubble_sort(c.copy(), n)
    print(*bubble_sorted)
    # is_stable_sorted_a = is_stable(c, bubble_sorted)
    # print('Stable' if is_stable_sorted_a else 'Not stable')
    print('Stable')

    selection_sorted = selection_sort(c.copy(), n)
    print(*selection_sorted)
    # is_stable_sorted_b = is_stable(c, selection_sorted)
    # print('Stable' if is_stable_sorted_b else 'Not stable')
    is_stable_sorted = is_stable2(bubble_sorted, selection_sorted)
    print('Stable' if is_stable_sorted else 'Not stable')


if __name__ == "__main__":
    main()
