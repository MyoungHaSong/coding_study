import sys 
from collections import deque
sys.stdin = open('input.txt','rt')
n,m = map(int, input().split())
a = deque(range(1,n+1))
cnt = 1
while len(a) != 1 :
    if cnt == m :
        cnt = 1
        a.popleft()
    else:
        a.append(a.popleft())
        cnt +=1
print(a.pop())