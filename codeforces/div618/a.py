for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    cnt = 0
    sum = 0
    for p in num:
        sum += p
        if p == 0:
            cnt += 1
            sum += 1
    if sum == 0:
        cnt += 1
    print(cnt)

