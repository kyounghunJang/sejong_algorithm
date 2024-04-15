from collections import deque
def solution(record):
    answer = []
    dic={}
    queue=deque([])
    
    for i in record:
        sim_list= i.split(" ")
        if sim_list[0]=="Leave":
            queue.append((1,sim_list[1]))
        elif sim_list[0] == "Enter":
            queue.append((0,sim_list[1]))
            dic[sim_list[1]]=sim_list[2]
        elif sim_list[0] == "Change":
            dic[sim_list[1]]=sim_list[2]
            
    while queue:
        a,b=queue.popleft()
        if a == 0:
            answer.append("{0}님이 들어왔습니다.".format(dic[b]))
        elif a == 1:
            answer.append("{0}님이 나갔습니다.".format(dic[b]))
    return answer