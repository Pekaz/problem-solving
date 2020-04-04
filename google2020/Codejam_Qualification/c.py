import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    schedule = []
    for i in range(n):
        x, y = list(map(int, sys.stdin.readline().rstrip().split()))
        schedule.append((x, y, i))
    schedule.sort(key=lambda element: element[0])
    chk = []
    re = [0] * n
    result = ''
    for i in range(1441):
        chk.append([])
    for job in schedule:
        c_enabled = True
        j_enabled = True
        for i in range(job[0], job[1]):
            if 'C' in chk[i]:
                c_enabled = False
            if 'J' in chk[i]:
                j_enabled = False
        if c_enabled:
            re[job[2]] = 1
            for i in range(job[0], job[1]):
                chk[i] += 'C'
        elif j_enabled:
            re[job[2]] = 2
            for i in range(job[0], job[1]):
                chk[i] += 'J'
        else:
            result = 'IMPOSSIBLE'
            break
    if result != 'IMPOSSIBLE':
        for c in re:
            if c == 1:
                result += 'C'
            else:
                result += 'J'
    print("Case #{}: {}".format(t+1, result))

