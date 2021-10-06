def grading(totalmark):
    if totalmark > 85:
        return 'A'
    elif totalmark >50:
        return 'B'
    else:
        return 'F'

def findtotal(marks):
    return sum(marks)

list_of_marks = [35,20,35,3]
print(grading(findtotal(list_of_marks)))
