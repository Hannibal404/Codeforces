from math import sqrt,floor

t = int(input())
for _ in range(t):
    n, = map(int,input().split())
    f = "FastestFinger"
    a = "Ashishgup"
    if n ==1:
        print(f)
    elif n == 2:
        print(a)
    elif n%2 != 0:
        print(a)
    else:
        od,ev = 0, 0
        while n%2 == 0:
            n //= 2
            ev+=1
        s = sqrt(n)
        if floor(s) == s:
            s = floor(s) + 1
        for i in range(3, int(s),2):
            while (n%i == 0):
                n //= i
                od += 1
        if n > 2:
            od +=1
        if od == 0:
            print(f)
        elif od == 1:
            if ev == 1:
                print(f)
            else:
                print(a)
        else:
            print(a)