def solution(participant, completion):
    answer = ''
    hash={}
    
    for i in participant:
        if i not in hash:
            hash[i]=0
        hash[i]+=1
    for i in completion:
        hash[i]-=1
    
    answer= {v:k for k,v in hash.items()}
    
    
    return answer.get(1)