# 00 01 10 11 일 때 1씩 증가하면
# 01 10 11 100 이므로 10 01 00 최하위 자리 두개 비트가 2 , 1 , 0 일때는 1~2개만 바뀌는것을 알 수있다
# 11인 경우 상단의 비트가 0인경우 와 1인경우로
# 상단의 비트가 0이라면 100(3개) 101(2개) 이므로 2만 증가하면 된다.
## 상단의 비트가 1인경우
## 그 위의 상단의 비트가 0인지 봐야한다

def findAnswer(number) :
    temp = 4
    if (number&3) < 3 :
        return number+1
    else :
        while (number//temp) & 1 == 1 :
            temp = temp*2
        return (number+1) +((temp/2)-1)
    
def solution(numbers):
    answer = []
    for number in numbers :
        answer.append(findAnswer(number))
    return answer