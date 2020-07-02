t = int(input())
for _ in range(t):
    n,a,b,c,d = map(int,input().split())
    x = abs(a-b)
    y = abs(b+a)
    w = abs(c-d)
    z = abs(c+d)
    a=0
    if n*(x) > z or n*y < w:
        print("No") 
    else:
        print("Yes")