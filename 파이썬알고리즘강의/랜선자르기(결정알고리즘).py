import sys
sys.stdin = open('input.txt','rt')

n, k = map(int, input().split())
a = []
max_ = -1
for _ in range(n):
    tmp = int(input())
    a.append(tmp)
    if tmp > max_:
        max_ = tmp
lt = 0
rt = max_
def count(x):
    cnt = 0
    for i in a:
        cnt += i//x
    return cnt
length = -1
while lt <=rt:
    middle = (lt + rt)//2
    cnt = count(middle)
    if cnt >= k:
        length = middle
        lt = middle +1
    else:
        rt = middle -1
print(length)
