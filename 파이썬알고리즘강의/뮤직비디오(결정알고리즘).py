import sys
sys.stdin = open('input.txt','rt')
n,k = map(int,input().split())
a = list(map(int,input().split()))
lower = 1
max_ = max(a)
upper = sum(a)
def count(x):
    cnt = 1
    length = 0
    for i in a:
        if length + i > x:
            cnt +=1
            length = i
        else:
            length +=i
    return cnt

length = 0 
while lower <= upper:
    middle = (lower + upper) //2
    if count(middle) <= k and middle>=max_:
        length = middle
        upper = middle -1
    else:
        lower = middle +1
print(length)

        
    