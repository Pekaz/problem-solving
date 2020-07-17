import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    x, y, z = list(map(int, sys.stdin.readline().rstrip().split()))
    if x == y and x >= z:
        print('YES')
        print(f'{x} {z} {z}')
    elif x == z and x >= y:
        print('YES')
        print(f'{y} {x} {y}')
    elif y == z and y >= x:
        print('YES')
        print(f'{x} {x} {y}')
    else:
        print('NO')
