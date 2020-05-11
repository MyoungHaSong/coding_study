import sys
sys.stdin= open('input.txt','rt')
n,m = map(int, input().split())
num = list(map(int, str(n)))
stack = []
for x in num :
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

for x in stack :
    print(x, end = ' ')