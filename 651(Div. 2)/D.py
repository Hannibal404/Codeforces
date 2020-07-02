n,k = map(int,input().split())
a = list(map(int,input().split()))

Mo = 0
Me = 0

for i in range(k):
    if i%2 == 1:
        if a[i]>Mo:
            Mo = a[i]
    else:
        if a[i]>Me:
            Me = a[i]

c = min(Me,Mo)

mc = float("inf")

i = 