"""useful example of how to work with 2-dimensional arrays"""


def main():
    n, m = [int(i) for i in input().split()]
    dots = [[j for j in input()[:m]] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if dots[i][j] == '.':
                di, dj, summator = 0, 0, 0
                for di in range(i - 1, i + 2):
                    for dj in range(j - 1, j + 2):
                        if (0 <= di < n) and (0 <= dj < m):
                            if dots[di][dj] == '*':
                                summator += 1
                dots[i][j] = summator
    for i in range(n):
        for j in range(m):
            print(dots[i][j], end='')
        print()


if __name__ == '__main__':
    main()
