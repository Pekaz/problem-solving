import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    check = [0] * (2 * n)
    result = []
    check[0] = 1
    x = 0
    y = 0
    for i in range(1, 2 * n):
        if a[i] == a[0]:
            y = i
            check[y] = 1
            break
    result.append(a[0])
    x = 0
    while True:
        if len(result) == n:
            break
        while True:
            if check[x] == 0:
                break
            x += 1
        while True:
            if check[y] == 0 and a[x] == a[y] and x < y:
                check[y] = 1
                check[x] = 1
                result.append(a[x])
                break
            y += 1

    for i in result:
        print(i, end=' ')
    print()

