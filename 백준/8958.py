n = int(input())
for j in range(n):
    data = input()
    new = 0
    cnt = 0
    for i in data:
        if i =='O':
            cnt +=1
            new +=cnt
        else:
            cnt = 0
    print(new)
        