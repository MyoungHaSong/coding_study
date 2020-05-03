import sys
sys.stdin = open('input.txt','rt')
def DFS(x,y):
    if dy[x][y]>0:
        return dy[x][y]
    if x ==0 and y ==0:
        return a[0][0]
    else:
        if y==0:
            dy[x][y] = DFS(x-1,y) + a[x][y]
            return 
        elif x ==0:
            dy[x][y] = DFS(x,y-1) + a[x][y]
        else:
            dy[x][y] = min(DFS(x-1,y), DFS(x,y-1)) + a[x][y]
            return dy[x][y]

if __name__=='__main__':
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    dy = [[0] * n for i in range(n)] 
    print(DFS(n-1, n-1))