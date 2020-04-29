import sys
from collections import deque
sys.stdin = open('input.txt','rt')
dx = []
a = [list(map(int,input().split())) for i in range(7)]
dis = [[0]*7 for i in range(7)]
q = deque()
a[0][0] = 1
q.append((0,0))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while q:
    tmp = q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<7 and 0<=y<7 and a[x][y] ==0:
            a[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] +1
            q.append((x,y))
if dis[6][6] ==0:
    print(-1)
else:
    print(dis[6][6])

