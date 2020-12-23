def matched(s):
    pos1=-1
    pos2=-1
    c1=0
    c2=0
    for i in range(len(s)):
        if(s[i]=="("):
            c1+=1
    for j in range(len(s)):
        if(s[j]==")"):
            c2+=1
    for i in range(len(s)):
        if(s[i]=="("):
            pos1=i
            break
    for i in range(len(s)):
        if(s[j]==")"):
            pos2=j
            break
    if((c1>c2)or(c1<c2)):
        return(False)
    else:
        if(pos2<pos1):
            return(False)
        else:
            return(True)
