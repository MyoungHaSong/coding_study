import sys
from collections import deque
sys.stdin = open('input.txt','rt')
if __name__=='__main__':
    n,m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(m)]
    q = deque()
    dis = [[0]*n for i in range(m)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(m):
        for j in range(n):
            if a[i][j] == 1 :
                q.append((i,j))

    while q:
        tmp = q.popleft()
        for i in range(4):
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            if 0<=xx<m and 0<=yy<n and a[xx][yy] == 0:
                a[xx][yy] = 1
                dis[xx][yy] = dis[tmp[0]][tmp[1]] +1
                q.append((xx,yy))
    flag = 1
    for i in range(m):
        for j in range(n):
            if a[i][j] == 0:
                flag = -1
    result = -1
    if flag == 1:
        for i in range(m):
            for j in range(n):
                if  dis[i][j] >result :
                    result = dis[i][j]
        print(result)
    else:
        print(result)