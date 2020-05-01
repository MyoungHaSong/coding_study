import sys
sys.stdin = open('input.txt','rt')
def DFS(L,s):
    global res
    if L ==m :
        sum =0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 231212
            for x in cb :
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis,abs(x1-x2)+abs(y1-y2))
            sum += dis
        if sum < res:
            res = sum
        
    else:
        for i in range(s,len(pz)):
            cb[L] =i 
            DFS(L+1, i+1)


if __name__ == '__main__':
    n,m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0]*m # combination m개가 살아남으니까 6개중 4개를 선택해서 넣겠다는거
    res = 123123
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 : 
                hs.append((i,j))
            elif a[i][j] == 2 :
                pz.append((i,j))
    DFS(0,0) # 조합을 그대로 넣을꺼임
    print(res)
