from math import log2


def dosome(n):
    if n == 1:
        return 1
    y = int(log2(n))
    x = 2**y
    n -= x
    return dosome(n) + 1


n = int(input())
while n % 2 == 0:
    n //= 2
if n == 1:
    print(1)
else:
    print(dosome(n))
