a = set()
for i in range(10):
    tmp = int(input())
    tmp = tmp%42
    a.add(tmp)
print(len(a))