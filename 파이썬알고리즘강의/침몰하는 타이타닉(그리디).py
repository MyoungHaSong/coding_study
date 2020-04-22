import sys
from collections import deque
sys.stdin = open('input.txt','rt')
n,w = map(int, input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
a = deque(a)
cnt = 0
while a :
    if len(a) == 1:
        a.pop()
        cnt +=1

    elif a[0] + a[-1] > w :
        a.popleft()
        cnt += 1
    else:
        a.popleft()
        a.pop()
        cnt +=1

print(cnt)
