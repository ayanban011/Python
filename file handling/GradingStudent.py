#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    for i in range(n):
        if(grades[i]<38):
            grades[i]+=0
        elif(grades[i]%5==3):
            grades[i]+=2
        elif((grades[i]%5==4)):
            grades[i]+=1
        elif(grades[i]<3):
            grades[i]+=0
    return(grades) 
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

