average = 0
stDev = 0

def main():
    ## Curve grades.
    global average
    global stDev
    infile = open("Scores.txt")
    scoresList = [eval(line) for line in infile]
    infile.close()
    numberOfScores = len(scoresList)
    average = sum(scoresList) / numberOfScores
    stDev = calculateStandardDeviation(scoresList, average)
    print("Number of scores:", numberOfScores)
    print("Average score:", average)
    print("Standard deviation of scores: {0:.2f}".format(stDev))
    # Curve the grades.
    for i in range(len(scoresList)):
        scoresList[i] = f(scoresList[i])
    dic = {'A':0, 'B':0,'C':0,'D':0,'F':0}
    for score in scoresList:
        dic[score] += 1
    print("GRADE DISTRIBUTION AFTER CURVING GRADES.")
    for key in sorted(dic):
        print(key + ':', dic[key], end="    ")

def calculateStandardDeviation(listOfNumbers, m):
    n = len(listOfNumbers)
    listOfSquaresOfDeviations = [0] * n
    for i in range(n):
        listOfSquaresOfDeviations[i] = (listOfNumbers[i] - m) ** 2
    standardDeviation = (sum(listOfSquaresOfDeviations) / n) ** .5
    return standardDeviation

def f(x):
    ## Curve grade.
    if x >= average + (1.5 * stDev):
        return 'A'
    elif x >= average + (.5 * stDev):
        return 'B'
    elif x >= average - (.5 * stDev):
        return 'C'
    elif x >= average - (1.5 * stDev):
        return 'D'
    else:
        return 'F'
    
main()
