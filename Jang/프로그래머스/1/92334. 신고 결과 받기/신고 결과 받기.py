def solution(id_list, report, k):
    dic={}
    answer=[0]*len(id_list)
    match_num={}
    for i,mem in enumerate(id_list):
        match_num[mem]=i
        
    for i in report:
        a,b= i.split(" ")
        if b not in dic:
            dic[b]=[a]
            continue
        if a in dic[b]:
            continue
        dic[b].append(a)
    for i in dic:
        tmp=len(dic[i])
        if tmp>=k:
            for j in dic[i]:
                answer[match_num[j]]+=1
    return answer