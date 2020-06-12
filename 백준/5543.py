a = []
for i in range(5):
    temp = int(input())
    a.append(temp)
 
print((min(a[0],a[1],a[2]) + min(a[3],a[4]) - 50))