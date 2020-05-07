import sys
sys.stdin = open('input.txt','rt')
n = int(input())
for i in range(n):
    N, s,e,k = map(int, input().split())
    a = list(map(int, input().split()))
    print('#%d'%(i+1), sorted(a[s-1:e])[k-1])
    
