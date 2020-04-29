import sys
from collections import deque
sys.stdin = open('input.txt','rt')

if __name__ =='__main__':
    MAX = 10000
    n,m = map(int, input().split())
    ch = [0] * (MAX+1)
    dis = [0] * (MAX+1)
    dis[n] = 0
    ch[n] = 1
    dq = deque()
    dq.append(n)
    while dq:
        now = dq.popleft()
        if now == m :
            break
        for next in (now-1, now+1, now+5):
            if 0<next<=MAX:
                if ch[next] ==0:
                    ch[next] = 1
                    dq.append(next)
                    dis[next] = dis[now] +1
    print(dis[m])