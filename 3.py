n = int(input())
l = []
for _ in range(n):
    l.append([int(i) for i in input().split()])
coo = [0, 0, 0]
isit = True
for i in range(len(l)):
    for j in range(len(l[0])):
        coo[j] += l[i][j]
for i in coo:
    if i != 0:
        print(i)
        isit = False
if isit:
    print('YES')
else:
    print('NO')
