import sys

n = int(sys.stdin.readline().rstrip())
num = list(sys.stdin.readline().rstrip().split())
num_len = len(num)
check = [0] * 32
bin_arr = []
for i in num:
    bi = list(bin(int(i)))[2:][::-1]
    bin_arr.append(bi)
    for j in range(len(bi)):
        check[j] += int(bi[j])

re = 0
st = -1
idx = 0
tcheck = check[::-1]
for idx, i in enumerate(tcheck):
    if i == 1:
        for j in range(num_len):
            if len(bin_arr[j]) > len(tcheck) - idx - 1 >= 0 and bin_arr[j][len(tcheck) - idx - 1] == '1':
                st = j
                break
        break

print(num[st], end=' ')
del num[st]
for i in num:
    print(i, end=' ')
