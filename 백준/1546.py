n = int(input())
a = list(map(int,input().split()))
max_ = max(a)
new = 0
for i in a:
    new += i/max_*100
print(new/n)
