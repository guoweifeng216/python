import pickle
import random

def main():
    pokerHand = getHandOfCards(5)
    displayPokerHand(pokerHand)
    pokerHand.sort()
    analyzePokerHand(pokerHand)

def getHandOfCards(numberOfCards):
    deckOfCards = pickle.load(open("deckOfCardsList.dat", 'rb'))
    return random.sample(deckOfCards, 5)

def displayPokerHand(pokerHand):
    print(", ".join(pokerHand))
    
def analyzePokerHand(pH):
    ranks = {x[:-1] for x in pH}
    numberOfRanks = len(ranks)
    if numberOfRanks == 5:
        print("ranks-all-different")
    elif numberOfRanks == 4:     
        print("one pair")
    elif numberOfRanks == 3:
        foundThree = False
        for i in range(2):
            if ((pH[i][0] == pH[i + 1][0]) and
                (pH[i + 1][0] == pH[i + 2][0])):
                print("three of a kind")
                foundThree = True
                break
        if foundThree == False:
            print("two pairs")
    else:  # two different ranks
        if ((pH[0][0] == pH[1][0]) and (pH[1][0] == pH[2][0]) \
             and (pH[2][0] == pH[3][0])) \
             or ((pH[1][0] == pH[2][0]) and (pH[2][0] == pH[3][0]) \
             and (pH[3][0] == pH[4][0])):
            print("four of a kind")
        else:
            print("full house")
        
main()    


