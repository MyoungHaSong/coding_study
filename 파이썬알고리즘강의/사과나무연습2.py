import sys
from collections import deque
sys.stdin = open('input.txt','rt')
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
ch = [[0]*n for i in range(n)]
sum_ = 0
sum_ += a[n//2][n//2]
ch[n//2][n//2] =1
q = deque()
q.append((n//2,n//2))
l =0
while True:
    if l == n//2:
        break
    size = len(q)
    for i in range(size):
        tmp = q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum_ += a[x][y]
                ch[x][y] = 1
                q.append((x,y))
    l +=1
print(sum_)