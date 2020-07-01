data = input().lower()
s = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
t = 0
for i range(len(data)):
    for j in s:
        if data[i] in j :
            t += s.index(j) +3 
print(t)
