from collections import deque 
def BFS(tickets) :
    tickets = sorted(tickets, key = lambda x : (x[1],x[0])) 
    start = "ICN"
    q = deque()
    q.append([start,[]])
    result = []
    while len(q) != 0 :
        currentStart,usedList = q.popleft()
        for index,ticket in enumerate(tickets) :
            if ticket[0] != currentStart :   
                continue
            if usedList is not None and index in usedList :
                continue 
            
            temp = [item for item in usedList]
            temp.append(index)
            q.append([ticket[1],temp])
        if len(usedList) == len(tickets) :
            for i,v in enumerate(usedList) :
                if i == 0 :
                    result.append(tickets[v][0])
                elif i == len(usedList)-1 :
                    result.append(tickets[v][0])
                    result.append(tickets[v][1])
                else :
                    result.append(tickets[v][0])
            break
    return result
def solution(tickets):
    answer = BFS(tickets)
    #answer=0
    return answer