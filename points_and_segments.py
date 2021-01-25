def start_point_find(point, arr):
    left = 0
    right = len(arr)
    while left < right:
        m = (left + right) // 2
        if point < arr[m][0]:
            right = m
        else:
            left = m + 1
    return left


def end_point_find(point, arr):
    left = 0
    right = len(arr)
    while left < right:
        m = (left + right) // 2
        if arr[m][1] < point:
            left = m + 1
        else:
            right = m
    return left


def main():
    n, m = map(int, input().split())
    list_lines = [tuple(map(int, input().split())) for _ in range(n)]
    start_point_sort = sorted(list_lines, key=lambda x: x[0])
    end_point_sort = sorted(list_lines, key=lambda x: x[1])
    list_points = [int(x) for x in input().split()]
    results = [start_point_find(x, start_point_sort) - end_point_find(x, end_point_sort) for x in list_points]
    print(*results)


if __name__ == '__main__':
    main()
