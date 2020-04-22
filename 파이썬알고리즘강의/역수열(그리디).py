import sys
sys.stdin = open('input.txt','rt')
n = int(input())
a = list(map(int, input().split()))
res = [0]*(n)

for i in range(n):
    for j in range(n):
        if a[i] ==0 and res[j] ==0:
            res[j] = i+1
            break
        if res[j] ==0 or res[j] > i+1 :
            a[i] -= 1
        
for x in res:
    print(x , end = ' ')


