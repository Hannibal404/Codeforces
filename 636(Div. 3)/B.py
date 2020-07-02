t = int(input())
for _ in range(t):
    n = int(input())
    if n%4!=0:
        print("NO")
    else:
        print("YES")
        for i in range(n//2):
            print((i+1)*2,end=" ")
        for i in range((n//2)-1):
            print((2*i)+1,end = " ")
        print(3*(n//2)-1)