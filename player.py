
'''
Player defines a player of the card game who waits to see a certain number of the
cards and then selects the first card after that sample that is higher than the
highest card in that sample.
'''
class Player:

    '''
    Creates a new Player instance.

    @param threshold is the integer number of cards to use as a sample before
            calling stop.

    @return a new Player instance with the given threshold.
    '''
    def __init__(self, threshold):
        self.threshold = threshold
        self.highestSeen = 0;

    '''
    Checks whether this player will call stop for a given card in the deck.

    @param cardPosition - the depth of this card into the deck
    @param cardValue - the value of this particular card

    @return boolean representing whether the player will shout "STOP" at this card.
    '''
    def shoutStopForValue(self, cardPosition,  cardValue):
        if cardPosition >= self.threshold and cardValue > self.highestSeen:
            return True
        if cardValue > self.highestSeen:
            self.highestSeen = cardValue
        return False

def main():
    p = Player(50)
    for i in range(100):
        if p.shoutStopForValue(i, i):
            print("Stopped at", i)

main()
