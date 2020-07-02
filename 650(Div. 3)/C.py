t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = input()
    i = 0
    c = 0

    while i < n and a[i] != '1':
        i += 1
    if i >= n:
        print(((n-1)//(k+1))+1)
        continue
    elif i > k:
        c += (i-1)//k

    j = i + 1
    while j < n:
        while j < n and a[j] != '1':
            j += 1
        c += (j-i-2)//((2*k))
        i = j
        j += 1
    print(c)
