


def isPrime(a):
    for i in range(2, int(a/2)):
        if a%i == 0:
            return False
    return True

a = 7
b = 11

check = [9]

while True:
    print(str(a) + " " + str(b))
    i = a
    while True:
        while True:
            if not isPrime(i) and i%2 is not 0:
                break
            i += 1
            if i == b:
                break
        if i == b:
            break
        if i not in check:
            print(i)
            exit()
        i += 1
    i = 1
    while True:
        if b <= a + 2 * i * i:
            break
        check.append(a + 2 * i * i)
        i += 1
    a = b
    while True:
        b += 1
        if isPrime(b):
            break

