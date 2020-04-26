import sys
sys.stdin = open('input.txt','rt')

def DFS(x):
    global cnt
    if x ==m:
        for i in range(m):
            print(ch[i], end = ' ' )
        print()
        cnt +=1
    else:
        for i in range(1, n+1):
            ch[x] = i
            DFS(x+1)

if __name__ =='__main__':
    n,m = map(int, input().split())
    cnt = 0
    ch = [0] * (n+1)
    DFS(0)
    print(cnt)
