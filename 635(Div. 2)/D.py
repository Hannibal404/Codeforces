t=int(input())
for _ in range(t):
    nr,ng,nb = map(int,input().split())
    r=list(map(int,input().split()))
    g=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if nr==1:
        rb=r[0]
    if nb==1:
        bb=b[0]
    if ng==1:
        gb=g[0]
        