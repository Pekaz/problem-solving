for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    odd = 0
    even = 0
    for i in num:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if (even > 0 and odd > 0) or (even == 0 and odd > 0 and odd % 2 == 1):
        print("YES")
    else:
        print("NO")
