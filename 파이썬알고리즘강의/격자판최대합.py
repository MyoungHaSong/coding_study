import sys
sys.stdin = open('input.txt','rt')
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

max_ = -1


for i in range(n):
    row = 0
    col = 0
    for j in range(n):
        row += a[i][j]
        col += a[j][i]
    if row- col > 0:
        if row > max_:
            max_ = row
    else:
        if col > max_:
            max_ = col
c = 0
cc = 0
for i in range(n):
    c += a[i][i]
    cc += a[i][n-i-1]
if c > max_:
    max_ = c
if cc > max_:
    max_ = cc
print(max_)