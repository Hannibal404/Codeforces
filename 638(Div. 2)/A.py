t = int(input())
for _ in range(t):
    n, = map(int,input().split())
    a,b = 0,0
    for i in range(1,n//2):
        a+= (1<<i)
    a+= (1<<n)
    for i in range(n//2,n):
        b += (1<<i)
    print(a-b)