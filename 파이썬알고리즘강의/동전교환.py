import sys
sys.stdin = open('input.txt','rt')

def DFS(x,sum):
    global min
    if x > min:
        return
    if sum == m:
        if min > x :
            min = x
    else:
        for i in range(n):
            DFS(x+1, sum + a[i])

    

if __name__ =='__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    a.sort(reverse=True)
    min = 123
    DFS(0,0)
    print(min)