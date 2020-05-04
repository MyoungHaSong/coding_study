import sys
sys.stdin = open('input.txt','rt')
if __name__ =='__main__':
    n,t = map(int, input().split())
    dy = [0] * (t+1)
    for i in range(n):
        s, t1 = map(int, input().split())
        for j in range(t,t1-1,-1):
            dy[j] = max(dy[j],dy[j-t1]+s)
    print(dy[t])


    