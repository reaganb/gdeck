import random


class Card:
    SUIT_SET = {'SPADES', 'HEARTS', 'CLUBS', 'DIAMONDS'}
    RANK_SET = {'A', 'K', 'Q', 'J',
                '10', '9', '8', '7', '6', '5',
                '4', '3', '2'}

    def __init__(self, suit, rank):
        """
            The constructor method consist of an error handling that strictly identifies
            if the suit and rank values are correct based from the class attribute sets.

            Arguments:
                suit -- the suit value
                rank -- the rank value
        """
        try:
            if suit.upper().strip() not in Card.SUIT_SET \
                    or rank.upper().strip() not in Card.RANK_SET:
                raise ValueError(f'{rank.upper().strip()} of {suit.upper().strip()} '
                                 f'is not a valid Card!')

            self.suit = suit.upper().strip()
            self.rank = rank.upper().strip()
        except ValueError as e:
            self.suit = None
            self.rank = None
            print(e)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    # The cards class attribute containing the list of Card class objects.
    cards = [Card(sl, rl) for sl in Card.SUIT_SET
             for rl in Card.RANK_SET]

    def __init__(self):
        """ Upon object instantiation, the cards will be shuffled."""
        self.shuffle()

    def __getitem__(self, position):
        return repr(Deck.cards[position])

    def __len__(self):
        return len(Deck.cards)

    @staticmethod
    def shuffle():
        """ The function for shuffling the Class attribute cards"""
        print("\nShuffling cards.... done!\n")
        random.shuffle(Deck.cards)


if __name__ == '__main__':
    # The starting point of the script, the Card and Deck class will be used here.

    card = Card(suit="hearts", rank='A')  # Instantiate the card object from the Card class
    print(card)  # Print the card object

    deck = Deck()  # Instantiate the deck object from the Deck class and shuffle its cards

    print("Number of cards from the deck: ", len(deck))
    print("10th card: ", deck[9])
    print("1st to 10th card: ", deck[:10])
    print("1st to 10th with 2 step card: ", deck[:10:2])
    print("Last to First card: ", deck[::-1])
    print("Randomly pick a card: ", random.choice(deck))  # Using the choice function of class random on object deck

    deck.shuffle()  # Shuffle the cards from the deck object

    print("9th card: ", deck[9])
    print("1st to 10th card: ", deck[:10])
    print("1st to 10th, 2 step card: ", deck[:10:2])
    print("Last to First card: ", deck[::-1])
    print("Randomly pick a card: ", random.choice(deck))  # Using the choice function of class random on object deck
