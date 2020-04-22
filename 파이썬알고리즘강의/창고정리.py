import sys
sys.stdin = open('input.txt','rt')
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
m = int(input())
for i in range(m):
    a[0] -= 1
    a[-1] +=1
    if a[0] <= a[1] :
        a.sort(reverse=True)

print(a[0] - a[-1])