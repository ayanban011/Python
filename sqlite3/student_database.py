""" Create string with infomation """

information = """Courses 
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput"""

""" Split string at '\n' then set range ends for categories """

info = information.split('\n')

for i in range(len(info)):
    if 'Courses' in info[i]:
        x = i
    if 'Students' in info[i]:
        y = i
    if 'Grades' in info[i]:
        z = i
    if 'EndOfInput' in info[i]:
        w = i

""" Create lists to hold dictionaries, along with grade_scale"""

courses = []
students = []
grades = []
grade_scale = {'A': 10, 'AB': 9, 'B': 8, 'BC': 7, 'C': 6, 'CD': 5, 'D':4}

""" Turn all categories into dictionaries of info provided """

for i in range(x+1, y):
    info[i] = info[i].split('~')
    temp = {}
    temp['Course Code'] = info[i][0]
    temp['Course Name'] = info[i][1]
    temp['Semester'] = info[i][2]
    temp['Year'] = info[i][3]
    temp['Instructor'] = info[i][4]
    courses.append(temp)

for i in range(y+1, z):
    info[i] = info[i].split('~')
    temp = {}
    temp['Roll Number'] = info[i][0]
    temp['Student Name'] = info[i][1]
    students.append(temp)

for i in range(z+1, w):
    info[i] = info[i].split('~')
    temp = {}
    temp['Course Code'] = info[i][0]
    temp['Semester'] = info[i][1]
    temp['Year'] = info[i][2]
    temp['Roll Number'] = info[i][3]
    temp['Grade'] = info[i][4]
    grades.append(temp)

""" Create student_grades dictionary
key = student name , value = list of grades
"""

student_grades = {}

for i in students:
    grade_list =[]
    student = i.get('Student Name')
    roll_number = i.get('Roll Number')
    roll_numbers = []  # added to store rollnums
    for j in grades:
        roll_numbers.append(j.get('Roll Number')) # store all rollnums ,you forgot the close parenthesis.
        if roll_number == j.get('Roll Number'):
            student_grades[student] = grade_list
            grade_list.append(j.get('Grade'))
        if roll_number not in roll_numbers: # gives 0 gpa if no grades
            student_grades[student] = 0

""" Convert grades to points, average points 
student_grades becomes key = name, value = total points/grades 
"""

for k, v in student_grades.items():
    if v == 0:   # if student gpa 0 set and continue 
        student_grades[k] = 0
        continue
    for i in range(len(v)):
        if v[i] in grade_scale:
            v[i] = grade_scale.get(v[i])
    student_grades[k] = (sum(v)/len(v))

""" Print
use information collected to print desired output
"""
for k, v in student_grades.items():
    for i in students:
        if i.get('Student Name') == k:
            print(f"{i.get('Roll Number')} {(i.get('Student Name')).ljust(20)} "
                  f" {student_grades.get(k)}")
