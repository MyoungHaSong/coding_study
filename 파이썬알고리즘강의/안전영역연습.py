import sys
sys.stdin = open('input.txt','rt')
def DFS(x,y,h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0 and a[xx][yy] > h :
            DFS(xx,yy,h)

if __name__=='__main__':
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    res = 0
    for h in range(100):
        ch = [[0] * n for i in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if a[i][j]> h and ch[i][j] ==0:
                    cnt +=1
                    DFS(i,j,h)
        res = max(cnt, res)
    print(res)