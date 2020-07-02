from collections import defaultdict

t = int(input())
for _ in range(t):
    d = defaultdict(int)
    s = input()
    m = int(input())
    b = list(map(int, input().split()))
    for i in s:
        d[i] += 1
    a = list(s)
    sea = list(set(a))
    sea.sort()
    b1 = [b[i] for i in range(m)]
    ans = [" " for _ in range(m)]
    j = 1
    f = True
    while f and j <= len(sea):
        x = 1
        c = 0
        for i in range(m):
            if b[i] == 0:
                c += 1
        while j <= len(sea) and d[sea[-j]] < c:
            j += 1
        if j > len(sea):
            break
        for i in range(m):
            if b[i] == 0:
                b1[i] = -1
                x = 0
                ans[i] = sea[-j]
                for k in range(m):
                    if b1[k] > 0:
                        b1[k] -= abs(i-k)
        b = [b1[vf] for vf in range(m)]
        if x == 1:
            f = False
        j += 1
    print("".join(ans))
