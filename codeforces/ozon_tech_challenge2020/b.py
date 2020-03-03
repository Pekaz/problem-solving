import sys

s = sys.stdin.readline().rstrip()
re = []

while True:
    left = []
    cnt = 0
    for i, c in enumerate(s):
        if c == '(':
            cnt += 1
        left.append(cnt)
    right = []
    cnt = 0
    for i, c in enumerate(s[::-1]):
        if c == ')':
            cnt += 1
        right.insert(0, cnt)

    chk = 0
    for i in range(len(s)):
        if left[i] >= right[i]:
            chk = right[i]
            break
    if chk == 0:
        break

    tmp = []
    cnt = 0
    for i, c in enumerate(s):
        if c == '(':
            tmp.append(i + 1)
            cnt += 1
        if cnt == chk:
            break
    cnt = 0
    for i, c in enumerate(s[::-1]):
        if c == ')':
            tmp.append(len(s) - i)
            cnt += 1
        if cnt == chk:
            break
    tmp.sort()
    re.append(tmp)
    for idx, i in enumerate(tmp):
        s = s[:i-1-idx] + s[i-idx:]
print(len(re))
for r in re:
    print(len(r))
    for i in r:
        print(i, end=' ')
    print('')
