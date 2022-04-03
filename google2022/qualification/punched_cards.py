import sys

for t in range(int(sys.stdin.readline().rstrip())):
    r, c = list(map(int, sys.stdin.readline().rstrip().split()))
    r = int(r)
    c = int(c)
    result = []

    for i in range(r * 2 + 1):
        result.append(['.'] * (c * 2 + 1))
        for j in range(c * 2 + 1):
            if i <= 1 and j <= 1:
                result[i][j] = '.'
            elif i % 2 == 0:
                if j % 2 == 0:
                    result[i][j] = '+'
                else:
                    result[i][j] = '-'
            else:
                if j % 2 == 0:
                    result[i][j] = '|'
                else:
                    result[i][j] = '.'

    print("Case #{}: ".format(t + 1))
    for i in range(r * 2 + 1):
        for j in range(c * 2 + 1):
            print(result[i][j], end='')
        print('')
