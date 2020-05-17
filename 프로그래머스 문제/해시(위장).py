def solution(clothes):
    dic = {}
    list_ = []
    answer = 1
    for i in range(len(clothes)):
        if clothes[i][1] not in dic :
            dic[clothes[i][1]] = [clothes[i][0]]
        else:
            dic[clothes[i][1]].append(clothes[i][0])
    for key, value in dic.items():
        list_.append(len(value)+1)
    for i in list_:
        answer *= i 
    answer -= 1 
    return answer