import sys
sys.stdin = open('input.txt','rt')
n = int(input())
a = [list(map(int ,input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    r,d,s = map(int, input().split())
    r -= 1
    tmp = [0] * n
    for j in range(n):
        if d == 0 :
            tmp[j-s] = a[r][j]
        else:
            tmp[(j+s)%n] = a[r][j]
    a[r] = tmp
s = 0
e = n
res = 0
for i in range(n):
    for j in range(s,e):
        res += a[i][j]
    if i < n//2 :
        e -= 1
        s +=1
    else:
        e +=1
        s -=1
print(res)