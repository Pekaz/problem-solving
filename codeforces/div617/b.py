for _ in range(int(input())):
    n = int(input())
    re = 0
    while True:
        if n < 10:
            re += n
            break
        re += int(n / 10) * 10
        n = int(n / 10) + n % 10
    print(re)
