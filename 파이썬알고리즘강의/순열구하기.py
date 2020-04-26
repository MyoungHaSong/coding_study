import sys
sys.stdin = open('input.txt','rt')

def DFS(x):
    global cnt
    if x == m :
        for j in range(m):
            print(res[j], end = ' ')
        print()
        cnt +=1
    else:
        for i in range(1,n+1):
            if ch[i] == 0 :
                ch[i] = 1
                res[x] = i
                DFS(x+1)
                ch[i] = 0 



if __name__ =='__main__':
    n , m = map(int, input().split())
    cnt = 0 
    res = [0] * (n+1)
    ch = [0] * (n+1)
    DFS(0)
    print(cnt)