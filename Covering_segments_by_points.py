def create_lines_list(n: int):
    """Trivia. Creats list of tuples from input.
       This code works for inputs with 2 values,
       for values other than 2 the code needs refactoring.
       Besides the func also sorts the created list of tupples by
       both values"""
    list_lines = [tuple(map(int, input().split())) for _ in range(n)]
    list_lines.sort(key=lambda line: (line[0], line[1]))
    return list_lines


def reduce_points(L):
    """this func reduces dots that are presented (x, y) where x == y"""
    i = 0
    while i < len(L):
        if L[i][0] == L[i][1]:
            L.pop(i)
            continue
        i += 1
    return L


def max_lines_at_segment(sorted_list):
    """this func uses greedy algorithm and computes the max number of segments in line
        it needs a sorted list as a parameter"""
    L = reduce_points(sorted_list)
    i = 1
    while i < len(L):
        if L[i - 1][0] <= L[i][0] and L[i][0] < L[i - 1][1] or L[i][0] <= L[i - 1][0]:
            L.pop(i)
            continue
        i += 1
    return L


def crossing_lines(L):
    """Actually, this function returns an overlapping lines
        and in this file it does nothing :D :D :D"""
    left = L[0][0]
    right = -1
    points = list()
    for i in range(len(L) - 1):
        if L[i][1] == L[i + 1][0]:
            continue
        right = L[i][1]
        points.append((left, right))
        left = L[i + 1][0]
    if left > right:
        right = L[-1][1]
        points.append((left, right))
    return points


def set_of_points(L):
    """returns minimum possible power of set of points covering all segments.
       Imagine it like you have papers (segments) and you need to staple them with
       minimum number of staples (dots)"""
    points = [-1]
    for i in range(len(L)):
        points.append(L[i][1])
        if L[i][0] == points[-2]:
            points.pop()
    points = points[1:]
    return points


def main():
    L = create_lines_list(int(input()))
    S = max_lines_at_segment(L)
    optimal_points = set_of_points(S)
    print(len(optimal_points))
    print(*optimal_points)


if __name__ == '__main__':
    main()
