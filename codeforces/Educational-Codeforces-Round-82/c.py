import sys


def goback(ins, idx, ss, cur, chk):
    if idx == len(ins):
        return ss
    if chk[ord(ins[idx]) - ord('a')] == 1:
        if cur + 1 < len(ss) and ss[cur + 1] == ins[idx]:
            re = goback(ins, idx + 1, ss, cur + 1, chk)
            if re is not None:
                return re
        elif cur - 1 >= 0 and ss[cur - 1] == ins[idx]:
            re = goback(ins, idx + 1, ss, cur - 1, chk)
            if re is not None:
                return re
    else:
        chk[ord(ins[idx]) - ord('a')] = 1
        if cur == 0:
            re = goback(ins, idx + 1, ins[idx] + ss, cur, chk)
            if re is not None:
                return re
        elif cur == len(ss) - 1:
            re = goback(ins, idx + 1, ss + ins[idx], cur + 1, chk)
            if re is not None:
                return re
        chk[ord(ins[idx]) - ord('a')] = 0
    return None


for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    check = [0] * 26
    check[ord(s[0]) - ord('a')] = 1
    result = goback(s, 1, s[0], 0, check)
    if result is None:
        print('NO')
    else:
        for ix, i in enumerate(check):
            if i == 0:
                result += chr(ix + ord('a'))
        print(f'YES\n{result}')
