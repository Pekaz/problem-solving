import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
words = []
check = [-1] * n
is_pal = [-1] * n
for i in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)
    if word == word[::-1]:
        is_pal[i] = 1

for i in range(n):
    for j in range(i+1, n):
        if words[i] == words[j][::-1]:
            check[i] = j
            check[j] = i
re = ''
max_len = 0
max_pal = -1
for i in range(n):
    if is_pal[i] == 1:
        if check[i] == -1 and max_len < len(words[i]):
            max_len = len(words[i])
            max_pal = i

if max_pal != -1:
    re = words[max_pal]

for i in range(n):
    if check[i] != -1:
        re = words[i] + re + words[check[i]]
        check[check[i]] = -1
        check[i] = -1
print(len(re))
print(re)
