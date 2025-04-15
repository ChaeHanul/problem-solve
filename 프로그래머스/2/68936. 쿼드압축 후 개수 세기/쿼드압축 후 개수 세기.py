def quadtree(arr,x,y,n) :
    if n == 1 :
        if arr[x][y] == 1 :
            return [[0,1]]
        else :
            return [[1,0]]
    else :
        temp = 0
        for i in range(x,x+n):
            for j in range(y,y+n):
                temp += arr[i][j]        
        if temp == 0 :
            return [[1,0]]
        elif temp == n*n :
            return [[0,1]]
        else:
            return quadtree(arr,x,y,n//2) + quadtree(arr,x+(n//2),y,n//2) + quadtree(arr,x,y+(n//2),n//2) +quadtree(arr,x+(n//2),y+(n//2),n//2)
def solution(arr):
    answer = [0,0]
    for item in quadtree(arr,0,0,len(arr)) :
        answer[0] += item[0]
        answer[1] += item[1]
    return answer