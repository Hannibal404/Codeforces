t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    mp = [0 for i in range(n)]
    l = 0
    mpeak = 0
    for i in range(1, n-1):
        if m[i] > m[i-1] and m[i] > m[i+1]:
            mp[i] = 1
    i = 1
    j = i + k - 2
    l = i
    np = mp[i:k+i-2].count(1)
    mpeak = np
    while j < n:
        np += mp[j]
        np -= mp[i]
        i += 1
        j += 1
        if np > mpeak:
            mpeak = np
            l = i
    print(mpeak+1, l)
