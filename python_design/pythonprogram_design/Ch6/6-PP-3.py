import pickle
import random

def main():
    ## Analyze a bridge hand.
    bridgeHand = getHandOfCards(13)
    displayBridgeHand(bridgeHand)
    analyzeBridgeHand(bridgeHand)

def getHandOfCards(numberOfCards):
    deckOfCards = pickle.load(open("deckOfCardsList.dat", 'rb'))
    return random.sample(deckOfCards, numberOfCards)

def displayBridgeHand(bridgeHand):
    print(", ".join(bridgeHand))
    
def analyzeBridgeHand(bridgeHand):
   suits = {x[-1] for x in bridgeHand}
   d = {suit:0 for suit in suits}  # distribution of cards into suits
   for card in bridgeHand:
       d[card[-1]] += 1
   t = tuple(d.items())
   tSorted = sorted(t)
   tSorted = sorted(t, key=lambda x: x[1], reverse=True)
   for k in tSorted:
       print("Number of", k[0], "is", k[1])
        
main()
