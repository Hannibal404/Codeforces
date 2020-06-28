from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = a[i] % k
    a.sort(reverse=True)
    if a[0] == 0:
        print(0)
        continue
    d = defaultdict(int)
    i = 0
    while i < n and a[i] != 0:
        d[a[i]] += 1
        i += 1
    aset = set(a)
    if 0 in aset:
        aset.remove(0)
    m = max(d.values())
    mn = float("inf")
    for i in aset:
        if d[i] == m and i < mn:
            mn = i

    mov = 1
    mov += ((m-1)*k) + (k-mn)
    print(mov)
