t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    diff=len(set(a))
    cnt=[0 for i in range(n+1)]
    for i in a:
        cnt[i]+=1
    Mcnt=max(cnt)
    print(max(min(Mcnt,diff-1),min(diff,Mcnt-1)))