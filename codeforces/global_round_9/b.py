import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    p = []
    for _ in range(n):
        p.append(list(map(int, sys.stdin.readline().rstrip().split())))
    result = True
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0) or (i == 0 and j == m - 1) or (i == n - 1 and j == 0) or (i == n - 1 and j == m - 1):
                if p[i][j] > 2:
                    result = False
            elif i == 0 or j == 0 or i == n - 1 or j == m - 1:
                if p[i][j] > 3:
                    result = False
            else:
                if p[i][j] > 4:
                    result = False

    if result:
        print('YES')
        for i in range(n):
            for j in range(m):
                if (i == 0 and j == 0) or (i == 0 and j == m - 1) or (i == n - 1 and j == 0) or (i == n - 1 and j == m - 1):
                    print('2', end=' ')
                elif i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    print('3', end=' ')
                else:
                    print('4', end=' ')
            print('')
    else:
        print('NO')
