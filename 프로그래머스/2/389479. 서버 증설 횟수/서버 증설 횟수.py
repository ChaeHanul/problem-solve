def solution(players, m, k):
    answer = 0
    #증설횟수,증설시간 쌍으로
    incServerList = []
    for i,v in enumerate(players) :
        reqServerCount = v//m
        if reqServerCount > 0 :
            if len(incServerList) > 0 :
                curServerCount = 0
                for incServerInfo in incServerList :
                    if i-incServerInfo[1] < k :
                        curServerCount += incServerInfo[0]
                if curServerCount < reqServerCount :
                    incServerList.append([reqServerCount-curServerCount,i])
                    answer += (reqServerCount-curServerCount)
            else :
                incServerList.append([reqServerCount , i])
                answer += reqServerCount
        #print(incServerList)
    return answer