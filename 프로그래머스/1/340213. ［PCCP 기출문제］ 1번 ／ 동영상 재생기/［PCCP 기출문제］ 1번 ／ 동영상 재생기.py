def formatMinSec(seconds) :
    if seconds <= 0 :
        return "00:00"
    m = str(seconds//60).zfill(2)
    s = str(seconds%60).zfill(2)
    return m + ":" + s
def calcSec(time) :
    return int(time[0:2])*60 +int(time[3:])
def skipOp(op_start,op_end,pos):
    result = pos
    #print(f"op_start seconds is {op_start[3:]} and op_end seconds is {op_end[3:]} ")
    if calcSec(op_start) <= calcSec(pos) <= calcSec(op_end) :
        result = op_end
        #print(f"hi {pos},{op_end}")
    return result
def prevOp(op_start,op_end,video_len,pos):
    result = ""
    result = formatMinSec(calcSec(pos)-10)
    return skipOp(op_start,op_end,result)
    #return result
def nextOp(op_start,op_end,video_len,pos):
    result = ""
    result = formatMinSec(calcSec(pos)+10)
    if calcSec(video_len) <= calcSec(result) :
        result = video_len
    result = skipOp(op_start,op_end,result)
    return result
def solution(video_len, pos, op_start, op_end, commands):
    pos = skipOp(op_start,op_end,pos)
    #print(pos)
    for command in commands:
        if command == "prev" :
            pos = prevOp(op_start,op_end,video_len,pos)
        elif command == "next" :
            pos = nextOp(op_start,op_end,video_len,pos)
        else :
            continue
    answer = pos
    return answer