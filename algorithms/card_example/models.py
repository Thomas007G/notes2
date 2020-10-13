import random

class Card:
    def __init__(self, irank, isuit):
        self._rank = irank
        self._suit = isuit

    def __str__(self):
        return '' + self._rank + self._suit
    
    def get_rank(self):
        return self._rank

    def get_suit(self):
        return self._suit
    
    def is_equal(self, other):
        if self._rank == other.get_rank() and self.get_suit == other.get_suit():
            return True
        return False

    def is_higher(self, other):
        if self._rank > other.get_rank():
            return True
        return False

class Deck:

    def __init__(self):
        self.Face_Up: []
        self.Face_Down: []
        self.generate()


    def generate(self):
        for i in ["spade", "heart", "diamond", "club"]:
            for j in range(1, 14):
                self.Face_Down.append(j, i)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.Face_Down)

class Board:
    def __init__(self):
        self.Face_Up: [Card]
        self.Face_Down: [Card]

    def generate(self, deck):
        num = random.randint(1, 52)
        return deck[:num]

    def get_revealed(self, deck: Deck) -> [Card]:
        return deck.Face_Up

    def get_num_hidden_cards(self, deck) -> int:
        return len(deck.Face_Down)

    def reveal_next(self, deck: Deck) -> Card:
        deck.Face_Up.append(self.Face_Down[0])
        deck.Face_Down.pop(0)
        return deck.Face_Up[-1]

    def play_game(self):
        deck = Deck()

        deck.Face_Down = self.generate(deck.Face_Down)

        print("Welcome to the Really Bad Card Game TM")
        life_lines = 2
        card = self.reveal_next(deck)
        print(f"Card revealed, { card.rank } of { card.suit }")
        while life_lines > 0:
            print("Enter a command below: show_revealed, num_hidden, skip, answer = {higher|lower}")
            inp = input()

            if inp.startswith("answer"):
                ans = inp.split(" ")[-1]

                next_card = self.reveal_next(deck)
                if ans >= next_card:
                    print("Correct")
                print("Incorrect :(")
                exit

            elif inp == "show_revealed":
                print(self.get_revealed(deck))

            elif inp == "num_hidden":
                print(self.get_num_hidden_cards(deck))
            
            elif inp == "skip":
                print("Skipping...")
                self.reveal_next(deck)
                life_lines -= 1
                pass
            else:
                print("Please provide one of the following commands... show_revealed, num_hidden, skip")