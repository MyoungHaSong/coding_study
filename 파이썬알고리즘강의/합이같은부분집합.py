import sys
sys.stdin = open('input.txt','rt')

def DFS(x,sum_):
    if x == n :
        if total - sum_ == sum_:
            print('YES')
            sys.exit(0)
    else:
        DFS(x+1, sum_ + a[x])
        DFS(x+1, sum_)
        



if __name__ =='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)
    print('NO')