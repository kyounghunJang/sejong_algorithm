
def solution(dirs):
    curr_dx=0
    curr_dy=0
    prev_dx=0  
    prev_dy=0  
    visited_line=[]
    dirs=list(dirs)
    for i in dirs:
        if i=='U' and curr_dy<5:
            visited_line.append((curr_dx,curr_dy,curr_dx,curr_dy+1))
            visited_line.append((curr_dx,curr_dy+1,curr_dx,curr_dy))
            curr_dy+=1
        if i=='D' and curr_dy>-5:
            visited_line.append((curr_dx,curr_dy,curr_dx,curr_dy-1))
            visited_line.append((curr_dx,curr_dy-1,curr_dx,curr_dy))
            curr_dy-=1
        if i=='R' and curr_dx<5:
            visited_line.append((curr_dx,curr_dy,curr_dx+1,curr_dy))
            visited_line.append((curr_dx+1,curr_dy,curr_dx,curr_dy))
            curr_dx+=1
        if i== 'L' and curr_dx>-5:
            visited_line.append((curr_dx,curr_dy,curr_dx-1,curr_dy))
            visited_line.append((curr_dx-1,curr_dy,curr_dx,curr_dy))
            curr_dx-=1
    visited_line=set(visited_line)
    return len(visited_line)/2