n, a, b, k = list(map(int, input().split()))
num = list(map(int, input().split()))
re = 0
for i, hp in enumerate(num):
    if hp <= a:
        num[i] = hp
    elif hp % (a + b) == 0:
        num[i] = a + b
    else:
        num[i] = hp % (a + b)
num.sort()
for hp in num:
    if hp <= a:
        re += 1
        continue
    sp = int(hp/a) - 1
    if hp % a != 0:
        sp += 1
    k -= sp
    if k < 0:
        break
    re += 1
print(re)
