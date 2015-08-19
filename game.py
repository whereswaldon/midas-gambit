'''
Game emulates a card game in which a deck of positive integer cards of
arbitrary size are flipped over one at a time. The cards are in a random order, and
the highest value in the deck is unknown. You win if you tell the dealer to "STOP" on
the highest card in the deck. You lose if you choose any card other than the highest.
The game costs money to play, and pays well if you win.
'''
class Game:

    '''
    Creates a new Game instance with the given player, deck, and prices.

    @param deck - the deck of cards used by this game.
    @param player - the player used by this game.
    @param buyInPrice - the cost of entering the game.
    @param payOutPrice - the monetary reward for winning the game.
    '''
    def __init__(self, deck, player, buyInPrice, payOutPrice):
        self.deck = deck
        self.player = player
        self.buyInPrice = buyInPrice
        self.payOutPrice = payOutPrice

    '''
    Plays out the game and prints the results.
    '''
    def play(self):

