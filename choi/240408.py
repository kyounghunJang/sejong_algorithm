#프로그래머스 [level 1] 모의고사 - 42840
def solution(answers):
    answer = []
    count = [0 ,0 ,0]
    rule1 = [1, 2, 3, 4, 5]
    rule2 = [2, 1, 2, 3, 2, 4, 2, 5]
    rule3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == rule1[i%5]:
            count[0]+=1
        if answers[i] == rule2[i%8]:
            count[1]+=1
        if answers[i] == rule3[i%10]:
            count[2] += 1
        
    mx = max(count)
    for i in range(3):
        if mx == count[i]:
            answer.append(i+1)
    answer.sort()
    
    return answer