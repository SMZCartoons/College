
'''import random
def generate_deck(suites = 4, type_cards = 13):
    cards = []
    for suites in range(suites):
        for type_cards in range(1, type_cards+1):
            cards.append(type_cards)
    random.shuffle(cards)
    return cards'''

class card:
    def __init__(self, suit, value): 
        self.suit = suit
        self.value = value
    
class deck:
    def __init__(self):
        self.cards = []  
    def shuffle(self):
        import random
        self.cards = random.shuffle(self.cards)
        return self.cards
    def draw(self):
         
        return 
    def add(self, card_to_add):
        self.cards.append(card_to_add)
    def print(self):
        print(self.cards)
        
print("This is war")
newdeck = deck()

for suit in range(4):
    for value in range(13):
        newcard = card(suit, value)

for x in range (0,4):
    suits = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
    for x in range(len(suits)):
        print(suits[x])
'''while(True):
    #need to use newdeck, as deck is the blueprint, so you actually have the deck
    newdeck.shuffle()
    newdeck.draw()
    newdeck.print()'''
    
    
    



        

    
        


        
