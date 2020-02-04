n = int(input())
arr = input()
re = [-1] * len(arr)
rev = arr[::-1]
imp = False
for i in enumerate(rev):
    if i == 0:
        continue
    if rev[i] > rev[i-1]:
        y = 0
        for j in range(1, i):
            if re[i-j] == 1:
                imp = True
                break
            if rev[i-j] > rev[i]:
                y = i - (j - 1)
                break
        if imp:
            break
        re[i] = 1
        for j in range(y, i):
            re[j] = 0
if imp:
    print(-1)
else:
    for i in re:
        print(re, end='')
