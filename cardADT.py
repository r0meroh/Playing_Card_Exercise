# cardADT.py

"""
  the ADT interface for the card object
"""

_SUITS = 'cdhs'
_SUIT_NAMES = ['clubs', 'diamonds', 'hearts', 'spades']
_RANKS = range(1,14)
_RANK_NAMES = ['Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
'Nine', 'Ten', 'Jack', 'Queen', 'King']

def create(rank, suit):
    # assert rank in _RANKS and suit in _SUITS
    return (rank, suit)

def rank(card):
    return card[0]

def suit(card):
    return card[1]

def suit_name(card):
    index = _SUITS.index(suit(card))
    return _SUIT_NAMES[index]

def rank_name(card):
    index = _RANKS.index(rank(card))
    return _RANK_NAMES[index]

def to_string(card):
    return rank_name(card) + ' of ' + suit_name(card)
