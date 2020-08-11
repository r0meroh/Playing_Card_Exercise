
import cardADT
import Card
import Deck


def main():


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
