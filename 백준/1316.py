n = int(input())
cnt = 0 
for i in range(n):
    data = input()
    if list(data) == sorted(data,key=data.find):
        cnt +=1 
print(cnt)
