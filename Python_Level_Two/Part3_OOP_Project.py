#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you and the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        shuffle(self.allcards)

    def split_deck(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed by: {}".format(self.name, drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for i in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def hand_check(self):
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

d = Deck()
d.shuffle()
half1,half2 = d.split_deck()

comp = Player("computer", Hand(half1))
name = input("What is your name player? ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.hand_check() and comp.hand_check():
    total_rounds += 1
    print("It is time for a new round!")
    print("Here are the current standings: ")
    print(user.name + " count: " + str(len(user.hand.cards)))
    print(comp.name + " count: " + str(len(comp.hand.cards)))
    print("Both players play a card!")

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()
    print(c_card)
    print(p_card)

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if user.hand_check() and comp.hand_check():
            c_card = comp.play_card()
            p_card = user.play_card()
        else:
            break

        table_cards.append(c_card)
        table_cards.append(p_card)

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name + " has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name + " has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("Great Game, it lasted: " + str(total_rounds))
print("A war occured " + str(war_count)+" times.")
