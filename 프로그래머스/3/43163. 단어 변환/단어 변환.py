##BFS로 최단 경로 구할 때, 백트래킹이 발생하므로 Q에 접근횟수를 기록해놓으면 문제해결.
from collections import deque 
def isAccessible(currentWord,targetWord) :
    result = False
    count = 0
    
    for i in range(len(currentWord)) :
        if currentWord[i] != targetWord[i] :
            count += 1
    if count == 1 :
        result = True
    #print(f"currentWord is {currentWord} and targetWord is {targetWord} compare result is {result}")
    return result
def bfs(words,begin,target):
    result = 0
    q = deque()
    visited = [False for _ in range(len(words))] 
    q.append([begin,0])
    #begin은 words에 없음 따라서 visited도 업데이트할게없다.
    while len(q) != 0 :
        currentWord,step = q.popleft()
        for i,v in enumerate(words) :
            if isAccessible(currentWord,v) == False or visited[i] == True :
                continue
            visited[i] = True
            q.append([v,step+1])
            print(f"currentWord is {currentWord} and targetWord is {v},step is {step}")
            if v == target :
                return step+1
    return 0
def solution(begin, target, words):
    answer = 0
    if target not in words :
        return answer
    else :
        answer= bfs(words,begin,target)
    return answer