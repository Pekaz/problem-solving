for _ in range(int(input())):
    n = int(input())
    arr = input()
    x = 0
    y = 0
    check = {}
    cnt = 1
    minlen = -1
    rex = 0
    rey = 0
    check[str(x)] = {str(y): 0}
    for c in arr:
        if c == 'L':
            x -= 1
        elif c == 'R':
            x += 1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
        chk = check.get(str(x), {}).get(str(y), -1)
        if chk != -1:
            if minlen == -1 or minlen > (cnt - chk):
                minlen = (cnt - chk)
                rex = chk + 1
                rey = cnt
        if str(x) not in check:
            check[str(x)] = {str(y): cnt}
        else:
            check[str(x)][str(y)] = cnt
        cnt += 1
    if minlen == -1:
        print(-1)
    else:
        print(f'{rex} {rey}')




