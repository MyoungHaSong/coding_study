max_ = 0
a = []
for i in range(9):
    tmp = int(input())
    a.append(tmp)
    if tmp>max_:
        max_ = tmp
print(max_)
print(a.index(max_)+1)
        
    