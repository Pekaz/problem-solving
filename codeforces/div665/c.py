import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    target = min(a)
    sort_result = sorted(a)
    check = [0] * n
    for i in range(n):
        if a[i] == sort_result[i]:
            check[i] = 1
    result = 'YES'
    for i in range(n):
        if check[i] == 0 and a[i] % target != 0:
            result = 'NO'
            break
    print(result)
