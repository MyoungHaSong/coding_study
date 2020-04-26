import sys
sys.stdin = open('input.txt','rt')

def DFS(x, sum, tsum):
    global max_
    if sum + (total - tsum) <max_:
        return 
    if sum > c :
        return 
    if x == n:
        if sum > max_:
            max_ = sum
    else:
        DFS(x+1 , sum + a[x], sum + a[x])
        DFS(x+1, sum, sum+a[x])
    

if __name__ == '__main__':
    c, n = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))

    total = sum(a)
    max_ = -1
    DFS(0,0,0)
    print(max_)