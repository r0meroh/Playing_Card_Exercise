"""
  this will be a linear search and binary search from memory.
"""

import cardADT
import Card
import Deck


def linear_search(listy, target):
    return 'found target at index: ', listy.index(target)

def binary_search(listy, target):
    listy = sorted(listy)
    low = 0
    high = len(listy)-1



    while(low <= high ):
        mid = (low + high)//2

        if target == listy[mid]:

            print('target found')
            return 'found at index', mid
        if target < listy[mid]:
            high = mid -1

        if target > listy[mid]:
            low = mid +1

    return -1, 'item not in list'


def store_duplicates_in_dictionary(word):
    my_dictionary = {}
    for letter in word:
        if letter not in my_dictionary:
            my_dictionary[letter] = 1
        elif letter in my_dictionary:
            my_dictionary[letter] += 1

    return sorted(my_dictionary.items())

def main():
    my_list = [2,3,1,33,22]
    my_word = 'letters the their theyre'
    print(linear_search(my_list, 1))
    print(binary_search(my_list, 22))
    print(store_duplicates_in_dictionary(my_word))

    for suit in 'cdhs':
        for rank in range(1,14):
            myCard = cardADT.create(rank,suit)
            print(cardADT.to_string(myCard))

    hugo = Card.Card(1,'c')
    print(hugo.card_to_string())

    for suit in 'cdhs':
        for rank in range(1,14):
            card = Card.Card(rank, suit)
            print(card.card_to_string())

    d = Deck.Deck()
    print(d.size_of_deck())
    print(d.deal_card().card_to_string())
    print(d.size_of_deck())
    print(d.deal_card().card_to_string())
    d.shuffle()
    print(d.size_of_deck())



if __name__ == '__main__':
    main()
