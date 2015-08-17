import random

'''
Deck represents a deck of cards with numbers (whole integers) written on each card.
The values of the cards are consecutive numbers in a random order. Cards are drawn
one at a time. 
'''
class Deck:
    '''
    Creates a new deck instance.

    @param size - an integer representing how many cards are in the deck.
    @param maximum - an integer representing the highest allowable value in the deck.

    @return a new Deck instance.
    '''
    def __init__(self, size, maximum):
        self.cards = []
        self.currentCard = 0
        for i in range(size):
            self.cards.append(i)
        self.shuffle()

    '''
    Returns a string representation of the Deck by displaying each value and
    the number of the current top card.

    @return a string representing the deck.
    '''
    def __str__(self):
        return self.cards.__str__()

    '''
    Reshuffles the cards in the deck into a new random order.
    Also resets the number of cards drawn to zero.
    '''
    def shuffle(self):
        self.cards = random.shuffle(self.cards)
        self.currentCard = 0

    '''
    Returns the value of the next card in the deck.

    @return the integer value of the next card.
    '''
    def __next__(self):
        if len(self.cards) > currentCard:
            raise StopIteration
        return self.cards[self.currentCard++]

    '''
    Returns an iterator for this deck object.

    @return an iterator.
    '''
    def __iter__(self):
        return self

'''
Makes a deck and prints it.
'''
def main():
    deck = Deck(100,1000)
    print deck

main()
