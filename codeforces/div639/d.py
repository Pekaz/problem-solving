import sys

cell = []
n, m = list(map(int, sys.stdin.readline().rstrip().split()))


def goback(x, y):
    global n, m
    global cell
    direction = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    cell[x] = cell[x][:y] + '.' + cell[x][y+1:]
    for d in direction:
        stx = x + d[0]
        sty = y + d[1]
        if 0 <= stx < n and 0 <= sty < m:
            if cell[stx][sty] == '#':
                goback(stx, sty)


for _ in range(n):
    r = sys.stdin.readline().rstrip()
    cell.append(r)
check = True
for i in range(n):
    tmp = -1
    for j in range(m):
        if tmp == -1:
            if cell[i][j] == '#':
                tmp = 0
        elif tmp == 0:
            if cell[i][j] == '.':
                tmp = 1
        elif tmp == 1:
            if cell[i][j] == '#':
                tmp = 2
    if tmp == 2:
        check = False
        break
for j in range(m):
    tmp = -1
    for i in range(n):
        if tmp == -1:
            if cell[i][j] == '#':
                tmp = 0
        elif tmp == 0:
            if cell[i][j] == '.':
                tmp = 1
        elif tmp == 1:
            if cell[i][j] == '#':
                tmp = 2
    if tmp == 2:
        check = False
        break

for i in range(n):
    tmp = False
    for j in range(m):
        if cell[i][j] == '#':
            tmp = True
    if not tmp:
        check = False

for j in range(m):
    tmp = False
    for i in range(n):
        if cell[i][j] == '#':
            tmp = True
    if not tmp:
        check = False

if not check:
    check = True
    for i in range(n):
        for j in range(m):
            if cell[i][j] == '#':
                check = False
    if check:
        print(0)
    else:
        print(-1)
else:
    re = 0
    while True:
        chk = False
        for i in range(n):
            for j in range(m):
                if cell[i][j] == '#':
                    goback(i, j)
                    re += 1
                    chk = True
        if not chk:
            break

    print(re)
