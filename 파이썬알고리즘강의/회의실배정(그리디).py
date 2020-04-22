import sys
sys.stdin = open('input.txt','rt')
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort(key= lambda x: (x[1],x[0]))
e=0
cnt = 0 
for sx,ex in a:
    if sx>=e :
        cnt +=1 
        e = ex
print(cnt)