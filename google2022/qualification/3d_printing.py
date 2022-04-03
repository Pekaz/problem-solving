import sys

for t in range(int(sys.stdin.readline().rstrip())):
    result = [1000001] * 4
    for i in range(3):
        cmyk = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(4):
            if cmyk[j] < result[j]:
                result[j] = cmyk[j]

    left = 1000000
    for j in range(4):
        if result[j] > left:
            result[j] = left
            left = 0
        else:
            left -= result[j]

    print("Case #{}: ".format(t + 1), end='')
    if left == 0:
        for i in range(4):
            print(result[i], end=' ')
    else:
        print('IMPOSSIBLE', end='')
    print('')
