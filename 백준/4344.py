n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    n = a[0]
    a = a[1:]
    s = sum(a)
    avg = s/len(a)
    cnt = 0
    for j in a:
        if j> avg:
            cnt+=1
    ratio = round(cnt/len(a) *100,3)
    print('%.3f'%(ratio)+'%')