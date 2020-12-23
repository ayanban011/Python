n=int(input())
grades = []
for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)
def gradingStudents(grades):
    for i in range(n):
        if(grades[i]<38):
            return(str(grades[i]))
        else:
            p=grades[i]%5
            return(str(grades[i]+5-p))
for j in range(n):
    result=gradingStudents(grades)
    print(result)

    
            
        
        
