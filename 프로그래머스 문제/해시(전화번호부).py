def solution(phone_book):
    answer = True
    dic = []
    for i in phone_book:
        for j in dic:
            length = len(j)
            if i[:length] in j :
                answer = False
            break
        dic.append(i)
            
    return answer