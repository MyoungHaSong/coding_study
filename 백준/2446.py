n = int(input())
a = n
for i in range(1,n+1):
    print(' '*(i-1)+'*'*(2*(a-i)+1))
for i in range(1,a):
    print(' '*(a-i-1)+'*'*(2*i+1))
