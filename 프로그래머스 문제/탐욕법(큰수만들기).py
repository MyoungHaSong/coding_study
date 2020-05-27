def solution(number, k):
    number = list(map(int, number))
    stack = []
    for i in number :
        while stack and k > 0 and stack[-1] < i :
            stack.pop()
            k-=1
        stack.append(i)
    if k!=0:
        stack = stack[:-k]
    answer = ''.join(map(str,stack))
    return answer