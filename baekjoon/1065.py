import sys

def check_list(num):
    if len(num) == 1:
        return True
    differ = int(num[1])-int(num[0])
    check = True
    for i in range(1,len(num)):
        if int(num[i])-int(num[i-1]) != differ:
            check = False
    return check


result = 0
num = input()
for i in range(1, int(num)+1):
    if check_list(f'{i}'):
        result += 1
print(result)
