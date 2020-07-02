t=int(input())
for _ in range(t):
    x, n, m =map(int,input().split())
    tx = x
    tn = n
    tm = m
    while tx >= 20 and tn >0:
        tx = (tx//2)+10
        tn-=1
    if tx <= m*10:
        print("YES")
    else:
        print("NO")