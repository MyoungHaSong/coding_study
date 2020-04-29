import sys
sys.stdin = open('input.txt','rt')
def DFS(x,y):
    global cnt
    if x>n or x<0 or y>n or y<0:
        return 
    if x==max_c[0] and y==max_c[1]:
        cnt +=1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n and a[xx][yy]>a[x][y]:
                DFS(xx,yy)

if __name__ == '__main__':
    n  = int(input())
    max_ = -1
    min_ = 123123
    a = []
    min_c = 0
    max_c = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    cnt = 0
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] > max_:
                max_ = tmp[j]
                max_c = (i,j)
            if tmp[j] < min_:
                min_ = tmp[j]
                min_c = (i,j)
        a.append(tmp)
    DFS(min_c[0], min_c[1])
    print(cnt)
        

    