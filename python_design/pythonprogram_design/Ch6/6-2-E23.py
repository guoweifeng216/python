import random
import pickle

def main():
    ## Calculate the High Point Count for a bridge hand.
    bridgeHand = getHand()
    print(", ".join(bridgeHand))  # Display the bridge hand.
    HCP = calculateHighCardPointCount(bridgeHand)
    print("HPC =", HCP)
    
def getHand():
    infile = open("DeckOfCardsList.dat", 'rb')
    deckOfCards = pickle.load(infile)
    infile.close()
    bridgeHand = random.sample(deckOfCards, 13)
    return bridgeHand

def calculateHighCardPointCount(bridgeHand):
    countDict = {'A':4, 'K':3, 'Q':2, 'J':1}
    HPC = 0
    for card in bridgeHand:
        rank = card[0]  # Each card is a string of
                        # two characters.
        if rank in "AKQJ":
            HPC += countDict[rank]
    return HPC 

main()














    


 



    

    









    
   






