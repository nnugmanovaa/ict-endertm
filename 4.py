n = int(input())
x = int(input())
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i*j == x:
            cnt += 1
print(cnt)
