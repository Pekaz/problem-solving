import sys

for t in range(int(sys.stdin.readline().rstrip())):
    direction = {'S': [0, -1],
                 'E': [1, 0],
                 'N': [0, 1],
                 'W': [-1, 0]}
    sx, sy, mv = list(sys.stdin.readline().rstrip().split())
    x = int(sx)
    y = int(sy)
    re = "IMPOSSIBLE"

    for idx, target in enumerate(mv):
        x += direction[target][0]
        y += direction[target][1]
        if idx + 1 >= abs(x) + abs(y):
            re = str(idx + 1)
            break
    print("Case #{}: {}".format(t + 1, re))
