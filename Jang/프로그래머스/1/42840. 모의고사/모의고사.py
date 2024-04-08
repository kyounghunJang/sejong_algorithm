def solution(answers):
    answer = []
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    third=[3,3,1,1,2,2,4,4,5,5]
    tmp=0
    sum1=0
    sum2=0
    sum3=0
    for i in answers:     
        if i == first[tmp%5]:
            sum1+=1
        if i == second[tmp%8]:
            sum2+=1
        if i  == third[tmp%10]:
            sum3+=1
        tmp+=1
    max_value=max(sum1,sum2,sum3)
    if max_value ==sum1:
        answer.append(1)
    if max_value ==sum2:
        answer.append(2)
    if max_value ==sum3:
        answer.append(3)
    return answer