def multiply(x):
    answer = 0
    for idx,i in enumerate(a) :
        
        answer += 10**idx * i *x
    return answer
a = list(map(int,input()))
a = a[::-1]
b = list(map(int,input()))

tr = multiply(b[2])
fr = multiply(b[1])
fi = multiply(b[0])
si = tr+fr*10+fi*100
print(tr)
print(fr)
print(fi)
print(si)

