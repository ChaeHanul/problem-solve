import re
def solution(files):
    #문자열 영소문자 혹은 영대문자 공백 빼기부호
    #header포착을 위한 패턴
    p = re.compile("([ a-zA-Z\-\.]+)([0-9]+)")
    temp = []
    answer = []
    for index, fileName in enumerate(files):
        head=p.match(fileName).group(1)
        number=p.match(fileName).group(2)
        temp.append([head.upper(),int(number),index,fileName])
    print(temp)
    for item in sorted(temp,key = lambda x :(x[0],x[1],x[2]))  :
        answer.append(item[3])
    return answer