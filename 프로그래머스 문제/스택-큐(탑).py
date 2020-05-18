def solution(heights):
    answer = []
    for idx,i in enumerate(range(len(heights))):
        tmp = heights.pop()
        flag = True
        for j in range(len(heights)-1,-1,-1):
            if heights[j] > tmp:
                answer.append(j+1)
                flag = False
                break
        if flag:
            answer.append(0)
    answer = answer[::-1]
    return answer