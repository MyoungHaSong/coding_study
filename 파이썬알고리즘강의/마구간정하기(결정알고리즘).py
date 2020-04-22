import sys
sys.stdin = open('input.txt','rt')
n, m = map(int, input().split())
def count(x):
    ep = a[0]
    cnt = 1
    for i in range(1,n):
        if a[i] - ep >= x:
            cnt +=1
            ep = a[i]
    return cnt
a = []
for _ in range(n):
    tmp = int(input())
    a.append(tmp)
a.sort()
lt = 1
rt = a[n-1]
length = 0
while lt <= rt:
    middle = (lt+rt)//2
    print(middle ,count(middle))
    if count(middle) >= m:
        length = middle
        lt = middle +1
    else:
        rt = middle -1
print(length)
