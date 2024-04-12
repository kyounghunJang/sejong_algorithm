from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    one=deque(cards1)
    two=deque(cards2)
    goal=deque(goal)
    
    while goal:
        chk=0
        tmp=goal.popleft()
        if len(one) != 0 and one[0]==tmp:
            one.popleft()
            chk=1
        elif len(two) !=0 and two[0]==tmp:
            two.popleft()    
            chk=1
        if chk==0:
            return "No"
    return "Yes"