import sys
from collections import deque
sys.stdin = open('input.txt','rt')
es = input()
n = int(input())

for i in range(n):
    a = deque(input())
    idx = 0
    while a :
        cur = a.popleft()
        if cur in es:
            if es.index(cur) == idx:
                idx +=1
            else:
                break
    if len(es) == idx : 
        print('%d YES'%(i+1))
    else:
        print('%d NO'%(i+1))
        
