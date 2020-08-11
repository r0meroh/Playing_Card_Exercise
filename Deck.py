# Deck.py

from random import randrange
from Card import Card

class Deck(object):

    def __init__(self):
        """
          create a deck of 52 cards
        """
        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank, suit))
        self.cards = cards

    def shuffle(self):
        """
          shuffle the deck of cards
        """
        cards0 = self.cards
        cards1 = []
        while cards0 != []:
            # generate a random position
            pos = randrange(len(cards0))
            # pop that card from that position
            card = cards0.pop(pos)
            # insert the card into the new list
            cards1.append(card)
        # new list is the old deck 'shuffled'
        self.cards = cards1

    def shuffle_2(self):
        times_to_iterate = self.size_of_deck
        cards = self.cards

        for i, card in enumerate(cards):
          pos = randrange(i,times_to_iterate)
          cards[i] = cards[pos]
          cards[pos] = card


    def deal_hand(self):
        """
          deal a set of 5 cards as a hand
        """
        pass


    def size_of_deck(self):
        """
          number of cards left in the Deck
        """
        return len(self.cards)

    def deal_card(self):
        """
          deals a single card from Deck
        """
        return self.cards.pop()
