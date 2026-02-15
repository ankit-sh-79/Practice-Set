import random


def build_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")
    return deck


def draw_cards(deck, count):
    cards = []
    for _ in range(count):
        cards.append(deck.pop())
    return cards


def card_value(card):
    rank = card.split(" ")[0]
    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    return values[rank]


def main():
    print("Simple Card Game: Higher Card Wins")

    deck = build_deck()
    random.shuffle(deck)

    player_card = draw_cards(deck, 1)[0]
    computer_card = draw_cards(deck, 1)[0]

    print("You drew:", player_card)
    print("Computer drew:", computer_card)

    player_value = card_value(player_card)
    computer_value = card_value(computer_card)

    if player_value > computer_value:
        print("You win!")
    elif player_value < computer_value:
        print("Computer wins!")
    else:
        print("It is a tie!")


if __name__ == "__main__":
    main()
