import sys

path = []
tri = []
for i in range(500):
    tri.append([0] * 500)
tri[0][0] = 1
for i in range(1, 500):
    for j in range(i+1):
        if j == 0:
            tri[i][j] = tri[i-1][j]
        elif j == i:
            tri[i][j] = tri[i-1][j-1]
        else:
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]


def goback(x, y, sumn, target):
    global path
    global tri
    dri = [[0, 1], [1, 1], [1, 0], [-1, 1], [-1, 0], [-1, -1]]
    path.append((x, y))
    sumn += tri[x][y]
    if sumn == target:
        return True
    if sumn > target or len(path) == 500:
        path.pop()
        return False
    for p in dri:
        nx = x + p[0]
        ny = y + p[1]
        if 0 <= nx < 500 and 0 <= ny < 500:
            if tri[nx][ny] != 0 and (nx, ny) not in path:
                if goback(nx, ny, sumn, target):
                    return True
    path.pop()
    return False


for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    goback(0, 0, 0, n)
    print("Case #{}:".format(t + 1))
    for re in path:
        print("{} {}".format(re[0]+1, re[1]+1))
    path = []



