import sys
from collections import deque
sys.stdin = open('input.txt','rt')

def DFS(x,y):
    global cnt
    if x <0 or x >6 or y > 6 or y<0:
        return
    if x ==6 and y == 6:
        cnt += 1
        
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and a[xx][yy] ==0:
                a[xx][yy] = 1
                DFS(xx,yy)
                a[xx][yy] = 0

if __name__ =='__main__':
    a = [list(map(int, input().split())) for _ in range(7)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    a[0][0] = 1
    cnt = 0
    DFS(0,0)
    print(cnt)
