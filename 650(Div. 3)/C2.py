t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = input()
    ans = 0
    i = 0
    while i <n:
        if a[i]=='1':
            break
        i+=1
    if i ==n:
        ans += (i+k)//(k+1)
    else:
        ans += (i//(k+1))
    c = 0
    x = i
    for i in range(x+1,n):
        if a[i]=='1':
            ans += (c-k)//(k+1)
            c = 0
        else:
            c += 1
    ans += c //(k+1)
    print(ans)
