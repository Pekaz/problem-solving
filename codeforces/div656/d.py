import sys


def goback(st, c):
    if len(st) == 1:
        if st == c:
            return 0
        else:
            return 1
    left = int(len(st) / 2) - st[:int(len(st) / 2)].count(c) + goback(st[int(len(st) / 2):], chr(ord(c) + 1))
    right = int(len(st) / 2) - st[int(len(st) / 2):].count(c) + goback(st[:int(len(st) / 2)], chr(ord(c) + 1))
    return min(left, right)


for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    print(goback(s, 'a'))
