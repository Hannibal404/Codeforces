t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    i, j, k = -1, -1, 0
    sum = 0
    while k < n:
        if a[k] < 0:
            if i == -1 or i < j:
                sum += a[k]
                i = k
            else:
                if a[k] > a[i]:
                    sum += a[k]-a[i]
                    i = k
        else:
            if j == -1 or j < i:
                sum += a[k]
                j = k
            else:
                if a[k] > a[j]:
                    sum += a[k] - a[j]
                    j = k
        k += 1
    print(sum)
