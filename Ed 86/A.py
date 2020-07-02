t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    if x == 0 and y == 0:
        print(0)
    else:
        if a > 2*b:
            print((x+y))