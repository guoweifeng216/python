def main():
    ## Determine semester grade.
    grade = getAverageGrade()
    semesterGrade = calculateLetterGrade(grade)
    print("Semester grade:", semesterGrade)

def getAverageGrade():
    midtermGrade = int(input("Enter grade on midterm exam: "))
    finalExamGrade = int(input("Enter grade on final exam: "))
    return ceil((midtermGrade + 2 * finalExamGrade) / 3)

def ceil(x):
    if int(x) != x:
        return int(x + 1)
    else:
        return x

def calculateLetterGrade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"    
    elif grade >= 60:
        return "D"
    else:
        return "F"
    
main()
