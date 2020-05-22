import sys
sys.stdin = open('input.txt','rt')
n,m = map(int, input().split())
g = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b,w = map(int, input().split())
    g[a][b] = w 

for i in range(n+1):
    for j in range(n+1):
        print(g[i][j] , end = ' ')
    print()