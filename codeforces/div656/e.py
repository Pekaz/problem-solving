import sys

finish_time = []
dir_edge = []
dir_edge_st = []
check = []
finish_count = 0
dir_edge_rev = []


def goback(x):
    global finish_time
    global dir_edge
    global dir_edge_st
    global check
    global finish_count

    if dir_edge_st[x] == -1:
        finish_time.append(finish_count, x)
        finish_count += 1
        return
    i = dir_edge_st[x]
    while True:
        if i == len(dir_edge) or dir_edge[i][0] != x:
            break
        if check[dir_edge[i][1]] == 0:
            goback(dir_edge[i][1])
    finish_time.append(finish_count, x)
    finish_count += 1
    return


def goback2(x):
    global finish_time
    global dir_edge
    global dir_edge_st
    global check
    global finish_count
    global dir_edge_rev

    if dir_edge_st[x] == -1:
        finish_time.append(finish_count, x)
        finish_count += 1
        return
    i = dir_edge_st[x]
    while True:
        if i == len(dir_edge) or dir_edge[i][0] != x:
            break
        if check[dir_edge[i][1]] == 0:
            goback(dir_edge[i][1])
    finish_time.append(finish_count, x)
    finish_count += 1
    return


for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    edge = []
    dir_edge = []
    dir_edge_st = [-1] * n
    check = [0] * n
    finish_time = []
    finish_count = 1

    for _ in range(m):
        e = list(map(int, sys.stdin.readline().rstrip().split()))
        edge.append(e)
        if e[0] == 1:
            dir_edge.append([e[1], e[2]])
    dir_edge = sorted(dir_edge)

    for idx, eg in enumerate(dir_edge):
        if dir_edge_st[eg[0]] == -1:
            dir_edge_st[eg[0]] = idx

    for i in range(n):
        if check[i] == 0:
            goback(i)

    sorted(finish_time, reverse=True)

    dir_edge_rev = []
    for eg in dir_edge:
        dir_edge_rev.append([eg[1], eg[0]])


