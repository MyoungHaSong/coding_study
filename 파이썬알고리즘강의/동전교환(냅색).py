import sys
sys.stdin = open('input.txt','rt')
if __name__=='__main__':
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    dy = [1000]* (m+1)
    dy[0] = 0
    for i in range(n):
        for j in range(a[i],m+1):
            dy[j] = min(dy[j],dy[j-a[i]]+1)
    print(dy[m])