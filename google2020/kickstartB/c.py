import sys


def run(submoves):
    direction = {'E': (1, 0),
                 'W': (-1, 0),
                 'S': (0, 1),
                 'N': (0, -1)}
    tx = 0
    ty = 0
    i = 0
    while True:
        if i == len(submoves):
            return tx, ty
        if submoves[i] in direction:
            tx += direction[submoves[i]][0]
            ty += direction[submoves[i]][1]
            i += 1
        else:
            num = int(submoves[i])
            st = i + 2
            st_cnt = 1
            ed = 0
            for idx, j in enumerate(submoves[st:]):
                if j == '(':
                    st_cnt += 1
                elif j == ')':
                    st_cnt -= 1
                if st_cnt == 0:
                    ed = st + idx
                    break
            sx, sy = run(submoves[st:ed])
            tx += num * sx
            ty += num * sy
            i = ed + 1


for t in range(int(sys.stdin.readline().rstrip())):
    x = 0
    y = 0
    moves = sys.stdin.readline().rstrip()
    movex, movey = run(moves)
    x += movex
    y += movey
    x %= 10**9
    y %= 10**9
    x += 1
    y += 1
    print("Case #{}: {} {}".format(t + 1, x, y))
