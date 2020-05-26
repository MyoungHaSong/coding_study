
def solution(arrangement):
    stack = []
    answer = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append(arrangement[i])
        else:
            stack.pop()
            if arrangement[i-1] == '(':
                answer += len(stack)
            else:
                answer +=1 
    return answer