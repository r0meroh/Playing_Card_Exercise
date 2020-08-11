# Card.py

"""
  simple playing card
"""


class Card:



  SUITS = 'cdhs'
  SUIT_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']
  RANKS = range(1,14)
  RANK_NAMES = ['Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
  'Nine', 'Ten', 'Jack', 'Queen', 'King']

  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit

#  def create_card(rank, suit):
#    """
#      creates a single card with a rank and suit
#    """
#    pass

  def suit_of_card(self):
    """
      returns the suit of the current selected card
    """
    return self.suit

  def rank_of_card(self):
    """
      returns the rank of the current selected card
    """
    return self.rank

  def suit_name(self):
    """
      returns one of the four suit names in a string format
    """
    index = self.SUITS.index(self.suit)
    return self.SUIT_NAMES[index]

  def rank_name(self):
    """
      returns the rank in string format of the current card
    """
    index = self.RANKS.index(self.rank)
    return self.RANK_NAMES[index]

  def card_to_string(self):
    """
      returns the string representation of the selected card
    """
    return self.rank_name() + ' of ' + self.suit_name()
