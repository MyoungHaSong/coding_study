data = []

while True:
    try:
        line = int(input())
        if line<40:
            line = 40
        data.append(line)
    except:
        break
print(int(sum(data)/len(data)))
    
