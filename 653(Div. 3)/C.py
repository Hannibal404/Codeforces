t = int(input())
for _ in range(t):
    n, = map(int, input().split())
    s = input()
    dep = 0
    mov = 0
    for i in s:
        if i == '(':
            dep += 1
        else:
            if dep == 0:
                mov += 1
            else:
                dep -= 1
    print(mov)
