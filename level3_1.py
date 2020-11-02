def solution(x, y):
    # Your code here
    x = int(x)
    y = int(y)

    def backTrack(x, y, step):
        
        if min(x,y)==0 and max(x,y)==1:
            return str(step-1)
        elif min(x,y)==0:
            return "impossible"
        if x > y:
            return backTrack(x - y * (x // y), y, step + x // y)
        else:
            return backTrack(x, y - x * (y // x), step + y // x)

    return backTrack(x, y, 0)
solution('2','3')
