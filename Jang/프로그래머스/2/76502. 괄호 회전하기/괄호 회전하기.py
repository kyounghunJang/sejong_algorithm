from collections import deque
def is_correct(s):
    a=[]
    for i in s:
        if len(a)==0:
            a.append(i)
            continue
        a.append(i)
        if a[-2] == '(' and a[-1] == ')':
            a.pop(-1)
            a.pop(-1)
        elif a[-2] =='{' and a[-1] =='}':
            a.pop(-1)
            a.pop(-1)
        elif a[-2] =='[' and a[-1]==']':
            a.pop(-1)
            a.pop(-1)
    if len(a)==0:
        return True
    else:
        return False
def solution(s):
    answer = 0
    tmp=deque(s)
    for i in range(len(s)):
        
        if is_correct(tmp):
            answer+=1
        value=tmp.popleft()
        tmp.append(value)
    
    return answer