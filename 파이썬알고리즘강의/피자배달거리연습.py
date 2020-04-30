import sys
sys.stdin = open('input.txt','rt')

def DFS(x,y):


if __name__=='__main__':
    n,m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    ch = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 2 :
                
