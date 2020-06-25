dic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
data = input()
for i in dic:
    data = data.replace(i,'*')
print(len(data))
