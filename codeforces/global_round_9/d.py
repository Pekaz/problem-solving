import sys


def get_mex(nums):
    check = [0] * (len(nums) + 1)
    for num in nums:
        check[num] = 1
    for idx, num in enumerate(check):
        if num == 0:
            return idx
    return len(nums)


def check_re(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    re = []
    x = n - 1
    while True:
        if check_re(a):
            break
        mex = get_mex(a)
        if mex == n:
            a[n - 1] = mex
            re.append(n)
        elif mex == x or mex == x + 1:
            a[x] = mex
            re.append(x + 1)
            x -= 1
        else:
            if mex >= x:
                mxd = x
                for j in range(0, x + 1):
                    if a[j] != j or a[j] != j + 1:
                        mxd = j
                        break
                a[mxd] = mex
                re.append(mxd + 1)
            else:
                a[mex] = mex
                re.append(mex + 1)

    print(len(re))
    for i in re:
        print(i, end=' ')
    print('')
