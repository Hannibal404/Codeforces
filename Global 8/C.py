from math import sqrt,ceil


def grey(i, j):
    m1[i-1][j], m1[i+1][j], m1[i][j-1], m1[i][j+1] = 1, 1, 1, 1


n = int(input())

x = ceil(sqrt(n))

m1 = [[0 for i in range(x+2)] for j in range(x+2)]

a = 0

for i in range(1, x + 1):
    for j in range(1, x + 1):
        if n > 0:
            m1[i][j] = 1
            grey(i,j)
            n -= 1
            if n == 0:
                a = -1
                break
    if a == -1:
        break

l = []
c=0
for i in range(x+2):
    for j in range(x+2):
        if m1[i][j] == 1:
            c += 1
            l.append(str(i)+ " "+ str(j))
print(c)
for i in l:
    print(i)