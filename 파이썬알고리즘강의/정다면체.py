import sys
sys.stdin = open('input.txt','rt')
n, m = map(int, input().split())
a = [0]*(n*m)
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i+j] +=1

max_ =max(a)
for i,x in enumerate(a):
    if x == max_ :
        print(i, end = ' ')
