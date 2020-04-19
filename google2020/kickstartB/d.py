import sys

for t in range(int(sys.stdin.readline().rstrip())):
    w, h, l, u, r, d = list(map(int, sys.stdin.readline().rstrip().split()))
    rob = [[0.0] * w, [0.0] * w]
    rob[1][0] = 1.0
    l -= 1
    u -= 1
    r -= 1
    d -= 1
    for i in range(h):
        for j in range(w):
            if not (l <= j <= r and u <= i <= d):
                if i - 1 >= 0:
                    if j == w - 1:
                        rob[1][j] += rob[0][j]
                    else:
                        rob[1][j] += rob[0][j] * 0.5
                if j - 1 >= 0:
                    if i == h - 1:
                        rob[1][j] += rob[1][j - 1]
                    else:
                        rob[1][j] += rob[1][j - 1] * 0.5
        rob.append([0.0] * w)
        rob.pop(0)
    print("Case #{}: {}".format(t + 1, rob[0][w-1]))
