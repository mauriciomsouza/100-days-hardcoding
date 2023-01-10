import random


def NumberTestGenerator():
    A = ''
    for i in range(4):
        A += str(random.randint(0, 255))
    return A


def Keys(s):
    n = len(s)
    if n < 4:
        return None
    combinations = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    if a + b + c + d == n and (a <= 3 and b <= 3 and c <= 3 and d <= 3):
                        combinations.append([a, b, c, d])
    return combinations


def isIpValid(ip):
    ip = ip.split(".")
    for i in ip:
        if (len(i) > 3 or int(i) < 0 or
                int(i) > 255):
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if (len(i) > 1 and int(i) != 0 and
                i[0] == '0'):
            return False

    return True


def Combinations(arr):
    if len(arr) < 4:
        return None
    a = []
    for key in Keys(arr):
        b = ''
        b += arr[0:key[0]] + '.'
        b += arr[key[0]:key[0] + key[1]] + '.'
        b += arr[key[0] + key[1]:key[0] + key[1] + key[2]] + '.'
        b += arr[key[0] + key[1] + key[2]:key[0] + key[1] + key[2] + key[3]]
        if isIpValid(b):
            a.append(b)
    return a


###TESTES###
arq = open('tests.txt','w')

for i in range(32):
    n = NumberTestGenerator()
    arq.write(f"{n}: {Combinations(n)}\n")

arq.close()