t=int(input())
for _ in range(t):
    for _ in range(9):
        l=list(input())
        for i in range(9):
            if l[i]=="1":
                l[i]="2"
                break
        print("".join(l))