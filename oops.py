
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
        self.card.remove(0)
        return 
    def add(self, card_to_add):
        self.cards.append(card_to_add)
        
print("This is war")
newdeck = deck()
for suit in range(4):
    for value in range(13):
        newcard = card(suit, value)
newdeck.add
        

    
        


        
