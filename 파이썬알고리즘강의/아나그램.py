import sys
sys.stdin = open('input.txt','rt')
a = input()
b = input()
str1 = dict()
str2 = dict()
for i in range(len(a)):
    str1[a[i]] = str1.get(a[i],0) + 1
    str2[b[i]] = str2.get(b[i],0) + 1 

if str1 == str2 :
    print("YES")
else:
    print("NO")
