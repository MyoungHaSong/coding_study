n = int(input())
for i in range(n):
    number , s = input().split()
    number = int(number)
    string = ''
    for j in s:
        string += j*number
    print(string)
