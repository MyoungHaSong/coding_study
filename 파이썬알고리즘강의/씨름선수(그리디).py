import sys
sys.stdin = open('input.txt','rt')
n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))
a.sort(reverse=True)
h,w = 0,0
cnt = 0
for h1,w1 in a:
    if w1 > w :
        w = w1
        cnt +=1
print(cnt)