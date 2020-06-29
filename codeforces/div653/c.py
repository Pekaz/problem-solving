import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    re = 0
    pair = 0
    for i in s:
        if i == '(':
            pair += 1
        elif i == ')':
            if pair == 0:
                re += 1
            else:
                pair -= 1
    print(re)
