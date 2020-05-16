def solution(participant, completion):
    dic = {}
    answer = ''
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic.get(i,0) +1
    for i in completion:
        dic[i] -= 1
    
    for key,val in dic.items():
        if val != 0 :
            answer += key
    
    return answer