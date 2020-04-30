import sys
from collections import deque
sys.stdin = open('input.txt','rt')

if __name__=='__main__':
    n= int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    q = deque()
    cnt = 0
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,1,-1]

    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 :
                cnt +=1
                q.append((i,j))
                while q:
                    tmp = q.popleft()
                    for z in range(8):
                        x = tmp[0] + dx[z]
                        y = tmp[1] + dy[z]
                        if 0<=x<n and 0<=y<n and a[x][y] == 1 :
                            a[x][y] = 0
                            q.append((x,y))
    print(cnt)