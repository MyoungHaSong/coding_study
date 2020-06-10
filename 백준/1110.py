tmp = inp = int(input())
count = 0
while True:
    t = tmp//10
    o = tmp%10
    res = t + o
    count += 1
    tmp = int(str(tmp%10)+str(res%10))
 
    if (inp==tmp):
        break
print(count)