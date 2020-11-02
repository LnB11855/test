def solution(l):
    # Your code here
    def compare(v1,v2):
        v1=[int(i) for i in v1.split('.')]
        v2=[int(i) for i in v2.split('.')]
        length=min(len(v1),len(v2))
        for i in range(length):
            if v1[i]<v2[i]:
                return -1
            if v1[i]>v2[i]:
                return 1
        if len(v1)<len(v2):
            return -1
        if len(v1)>len(v2):
            return 1
        return 0
    l.sort(cmp=compare)
    return l
solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
