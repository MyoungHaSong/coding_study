import sys
sys.stdin = open('input.txt','rt')

n = int(input())
cnt = 0
a = [0]*(n+1)
for i in range(2,n+1):
    if a[i] == 0 :
        cnt +=1
        for j in range(i,n+1,i):
            a[j] = 1
        
print(cnt)
