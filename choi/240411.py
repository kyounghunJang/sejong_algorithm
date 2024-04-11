#프로그래머스 lv1, 완주하지못한선수
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]

#해시 이용 코드. 
# hash를 통해, 각 선수 이름 별 유일한 숫자로 매칭하여, participant 합과 completion합의 차이를 이용한다. 
def solution(participant, completion):
    answer=''
    temp=0
    dic={}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= int(hash(part))
    answer = dic[temp]

    return answer
        
  