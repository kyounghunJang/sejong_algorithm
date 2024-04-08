def solution(numbers):
    ans=[]
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            ans.append(numbers[i]+numbers[j])
    answer=list(set(ans))
    answer.sort()
    return answer