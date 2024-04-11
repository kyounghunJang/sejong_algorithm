from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    days=deque([])
    for i,j in zip(progresses,speeds):
        tmp=math.ceil((100-i)/j)
        days.append(tmp)
    cnt=1
    tmp=days.popleft()
    while days:
        if days[0] <=tmp:
            cnt+=1
            days.popleft()
        else:
            answer.append(cnt)
            cnt=1
            tmp=days.popleft()
        if len(days)==0:
            answer.append(cnt)
            break
    return answer