def main():
    ## Determine semester grade.
    grades = []
    for i in range(1, 6):
        grade = eval(input("Enter grade " + str(i) + ": "))
        grades.append(grade)
    grades.sort()
    grades = grades[2:]
    (rng, ave) = analyzeGrades(grades)
    print("Range:", rng)
    print("Average:", ave)

def analyzeGrades(grades):
    rng = grades[-1] - grades[0]
    ave = sum(grades) / len(grades)
    return (rng, ave)
    
main()
