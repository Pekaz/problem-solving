import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    b = sys.stdin.readline().rstrip()
    re = b[:2]
    i = 3
    while True:
        if i >= len(b):
            break
        re += b[i]
        i += 2
    print(re)

