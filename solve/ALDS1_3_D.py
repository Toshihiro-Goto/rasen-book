# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_D

def main():
    s = input()

    left_idxs = []
    areas = []

    for i, c in enumerate(s):
        if c == "\\":
            left_idxs.append(i)

        elif c == "/" and len(left_idxs) > 0:
            left_idx = left_idxs.pop()
            area = i - left_idx
            for j in range(len(areas))[::-1]:
                if areas[j][0] < left_idx:
                    break
                area += areas.pop()[1]
            areas.append((left_idx, area))

    print(sum(map(lambda x: x[1], areas)))
    print(len(areas), *map(lambda x: x[1], areas))


if __name__ == "__main__":
    main()
