t = int(input())
for _ in range(t):
    n = int(input())
    p1, c1 = map(int, input().split())
    i = 1
    a = 0
    while i < n:
        p2, c2 = map(int, input().split())
        if a == 0:
            if c2 > p2 or p1 > p2 or c1 > c2 or ((c2 - c1) > (p2-p1)) or c1 > p1:
                print("NO")
                a = -1
            else:
                p1, c1 = p2, c2
        i += 1
    if a == 0:
        print("YES")
