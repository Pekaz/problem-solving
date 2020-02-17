import sys

s = sys.stdin.readline().rstrip()
cnt = {}
re = 0
for i in s:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1
    if re < cnt[i]:
        re = cnt[i]
if re < int((re * (re - 1))/2):
    re = int((re * (re - 1))/2)

chk = {}
cnt = {}
tar = []
for i in range(len(s)):
    idx = len(s) - i - 1
    if idx == len(s) - 1:
        cnt[s[idx]] = 1
        if cnt[s[idx]] == 1:
            tar.append(s[idx])
        continue
    for j in tar:
        if cnt[j] == 0 or s[idx] == j:
            continue
        if s[idx]+j not in chk:
            chk[s[idx] + j] = cnt[j]
        else:
            chk[s[idx]+j] += cnt[j]
        if chk[s[idx]+j] > re:
            re = chk[s[idx]+j]
    if s[idx] not in cnt:
        cnt[s[idx]] = 1
    else:
        cnt[s[idx]] += 1
    if cnt[s[idx]] == 1:
        tar.append(s[idx])
print(re)
