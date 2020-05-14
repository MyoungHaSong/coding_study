def solution(answers):
    answer = []
    score = [0,0,0]
    answer_1 = list(range(1,6)) 
    answer_2 = [2,1,2,3,2,4,2,5] 
    answer_3 = [3,3,1,1,2,2,4,4,5,5] 
    
    for i in range(len(answers)):
        if answer_1[i%len(answer_1)] == answers[i]:
            score[0] +=1
        if answer_2[i%len(answer_2)] == answers[i]:
            score[1] +=1
        if answer_3[i%len(answer_3)] == answers[i]:
            score[2] +=1
    max_value = max(score)
    for idx, i in enumerate(score):
        if i == max_value:
            answer.append(idx+1)
    return answer
    