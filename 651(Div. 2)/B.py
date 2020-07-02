from math import gcd

t = int(input())
for _ in range(t):
    n, = map(int,input().split())
    a = list(map(int,input().split()))
    e,o = [(i+1) for i in range(0,2*n,2)],[(i+1) for i in range(1,2*n,2)]
    od,ev = len(o),len(e)
    if od%2 == 1:
        ev-=1
        od-=1
    else:
        if ev>1:
            ev-=2
        else:
            od-=2
    for i in range(0,od,2):
        print(o[i],o[i+1])
    for i in range(0,ev,2):
        print(e[i],e[i+1])