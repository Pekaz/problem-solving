import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    sq = []
    target = [(0, 0), (1, 3), (2, 6),
              (3, 1), (4, 4), (5, 7),
              (6, 2), (7, 5), (8, 8)]
    for i in range(9):
        ln = sys.stdin.readline().rstrip()
        tmp = []
        for c in ln:
            tmp.append(int(c))
        sq.append(tmp)
    for i in target:
        if sq[i[0]][i[1]] < 9:
            sq[i[0]][i[1]] = sq[i[0]][i[1]] + 1
        else:
            sq[i[0]][i[1]] = sq[i[0]][i[1]] - 1
    for i in range(9):
        for j in range(9):
            print(sq[i][j], end='')
        print('')


