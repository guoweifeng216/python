import random
import pickle
NUMBER_OF_TRIALS = 10000

def main():
    ## Carry out matching process NUMBER_OF_TRIALS times.
    totalNumberOfMatches = 0 
    for i in range(NUMBER_OF_TRIALS): 
        totalNumberOfMatches += matchTwoDecks() 
    averageNumberOfMatches = totalNumberOfMatches / NUMBER_OF_TRIALS 
    print("The average number of cards") 
    print("that matched was {0:.3f}.".format(averageNumberOfMatches)) 
 
def matchTwoDecks():
    ## Determine number of matches when comparing two shuffled decks of cards.
    # Create two decks as lists with the binary file
    # DeckOfCardsList.dat from Example 2.
    infile = open("DeckOfCardsList.dat", 'rb') 
    deck1 = pickle.load(infile) 
    infile.close() 
    infile = open("DeckOfCardsList.dat", 'rb') 
    deck2 = pickle.load(infile) 
    infile.close() 
    # Shuffle both decks of cards
    random.shuffle(deck1) 
    random.shuffle(deck2)
    # Compare cards and determine number of matches
    numberOfMatches = 0 
    for i in range(52): 
        if (deck1[i] == deck2[i]): 
            numberOfMatches += 1 
    return numberOfMatches 

main()
