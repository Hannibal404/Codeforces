t = int(input())
for _ in range(t):
    n = int(input())
    i = 2
    while i:
        x =((2**i)-1)
        if n%x== 0:
            print(n//x)
            break
        i+=1