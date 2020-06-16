from collections import defaultdict
a = []
dic = defaultdict(int)
for i in range(10):
    dic[i] = 0
a =[]
for i in range(3):
    tmp = int(input())
    a.append(tmp)
data = a[0]*a[1]*a[2]

for i in str(data):
    tm = int(i)
    dic[tm] = dic.get(tm,0) +1 
for i in range(10):
    print(dic[i])