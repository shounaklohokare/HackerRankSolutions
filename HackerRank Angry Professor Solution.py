# https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k, a):

    studentsInTime = 0
    for student in a:
        if student<=0:
            studentsInTime+=1

    if studentsInTime>=k:
        return  "NO"

    return "YES"

ans=angryProfessor(3, [-1, -3, 4, 2])
print(ans)
# YES