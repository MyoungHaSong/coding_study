import sys 
# sys.stdin = open('input.txt','rt')
n = int(input())
max = -12321321
for i in range(n) :
    tmp = list(map(int,input().split()))
    tmp = sorted(tmp)
    a,b,c = tmp
    if a == b and b==c:
        result = 10000 + (a*1000)
    elif a==b or a==c :
        result = 1000+(a*100)
    elif b==c :
        result = 1000+(b*100)
    else:
        result = c* 100
    if result > max :
        max = result
print(max)