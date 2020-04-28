import sys
sys.stdin = open('input.txt','rt')

def DFS(L):
    global res
    if L ==n:
        dif = max(money) - min(money)
        if dif < res:
            tmp = set() # 값이 다 다른걸 판별해야함
            for x in money :
                tmp.add(x)
            if len(tmp) ==3:
                res = dif
    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]
if __name__ =='__main__':
    n = int(input())
    coin = []
    money = [0]*3
    res = 8888
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)    
    print(res)