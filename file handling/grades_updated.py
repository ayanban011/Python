from collections import OrderedDict
def grades():
    l = []
    courses = []
    while(True):
        str  = input()
        if(str == 'EndOfInput'):
            break
        else:
            l.append(str)
    length = len(l)
    d = {'A':10,'AB':9,'B':8,'BC':7,'C':6,'CD':5,'D':4}
    ind = l.index('Students') + 1
    rollNo = OrderedDict()
    lis = OrderedDict()
    roll = []
    students = OrderedDict()
    i = 0
    while(True):
        str = l[ind]
        if(str == 'Grades'):
            break
        else:
            str = l[ind].split('~')
            roll.append(str[0])
            lis[str[0]] = i
            i += 1
            students[str[0]]=str[1]
            ind += 1
            courses.append(0)
    roll.sort()
    for r in roll:
        rollNo.setdefault(r,0)
    ind = l.index('Grades')
    for i in range(ind+1,length):
        str = l[i].split('~')
        s  = str[3]
        rollNo[s] += d[str[4]]
        j = lis[s]
        courses[j] += 1
    j = 0 
    for i in courses:
        if(i != 0):
            rollNo[roll[j]] /= float(i)
            round(rollNo[roll[j]],2)
        else:
            rollNo[roll[j]] = 0
        j += 1
    i = 0
    for stud in rollNo:
        print(stud,end='')
        print('~',end='')
        print(students[stud],end='')
        print('~',end='')
        print(rollNo[stud])
        i += 1
    grades()
