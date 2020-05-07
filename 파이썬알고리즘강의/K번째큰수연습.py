import sys
sys.stdin = open('input.txt','rt')
n , k = map(int, input().split())
a = list(map(int, input().split()))
res= set()
for i in range(n):
    for j in range(i+1 , n ):
        for m in range(j+1, n ):
            res.add(a[i] + a[j] + a[m])
            
a = sorted(list(res), reverse = True)
print(a[k-1])