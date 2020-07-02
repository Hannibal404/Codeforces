t = int(input())
for _ in range(t):
    n, = map(int, input().split())
    a = list(map(int, input().split()))
    e,o = 0,0
    for i in range(n):
        if a[i]%2==0 and i%2!=0:
            e+=1
        elif a[i]%2!=0 and i%2==0:
            o +=1
    if o != e:
        print(-1)
    else:
        print(e)