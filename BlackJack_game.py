import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

mydeck=Deck()

class Player:
    def __init__(self):
        self.all_cards=[]

    def add_cards(self,card):
        self.all_cards.append(card)

    def suma(self,suma_p):
        suma=0
        for i in self.all_cards:
            suma+=i.value
        return suma-suma_p
    def __str__(self):
        # Construim un string care să conțină toate informațiile dorite
        card_list = ', '.join(str(i) for i in self.all_cards)
        return f'Player cards: {card_list}'

class Dealer:
    def __init__(self):
        self.all_cards=[]

    def add_cards(self,card):
        self.all_cards.append(card)

    def suma(self,suma_d):
        suma=0
        for i in self.all_cards:
            suma+=i.value
        return suma-suma_d
    def __str__(self):
        # Construim un string care să conțină toate informațiile dorite
        card_list=str(self.all_cards[0])+', HIDDEN CARD'
        card_list = card_list+', '.join(str(self.all_cards[i]) for i in range(2,len(self.all_cards)))
        return f'Dealer cards: {card_list}'
    def print_cards(self):
        card_list =', '.join(str(self.all_cards[i]) for i in range(0,len(self.all_cards)))
        return f'Dealer cards: {card_list}'

game_on=True
player=Player()
dealer=Dealer()
while game_on:
    #start game
    player.add_cards(mydeck.deal_one())
    player.add_cards(mydeck.deal_one())

    dealer.add_cards(mydeck.deal_one())
    dealer.add_cards(mydeck.deal_one())

    print(player)
    player_turn=True
    suma_p=0
    while player_turn:
        if player.suma(suma_p)<21:
            print(f'Your total is {player.suma(suma_p)}')
            val='J'
            while val!='Y' and val != 'N':
                val=input('Do you want to take one more card? (Y or N)')
                if val!='Y' and val != 'N':
                    print('I do not understand. Please try again!')
                elif val=='Y':
                    card=mydeck.deal_one()
                    player.add_cards(card)
                    print(player)
                    if card.rank=='Ace':
                        if player.suma(suma_p)+11>21:
                            suma_p+=10  
                else:
                    print('Your turn is over')
                    player_turn=False
        elif player.suma(suma_p)==21:
            print('Player wins!')
            game_on=False
            break
        else:
            print('Game Over!')
            game_on=False
            break
                 
    print('\n')                
    print(player)
    print(f'The total is {player.suma(suma_p)}')
    if player.suma(suma_p)>=21:
        break

    print('\n')
    print('Dealer turn')
    print(dealer)
    dealer_turn=True
    suma_d=0
    while dealer_turn:
        if dealer.suma(suma_d)>player.suma(suma_p) and dealer.suma(suma_d)<21:
            print('Game Over!')
            print(f'The total is {dealer.suma(suma_d)}')
            game_on=False
            break
        elif dealer.suma(suma_d)<21:
            card=mydeck.deal_one()
            dealer.add_cards(card)
            if card.rank=='Ace':
                if dealer.suma(suma_d)+11>21:
                    suma_d+=10
        elif dealer.suma(suma_d)==21:
            print('Game Over!')
            print(f'The total is {dealer.suma(suma_d)}')
            game_on=False
            break
        elif dealer.suma(suma_d)>21:
            print('Player wins!')
            print(f"Dealer's total is {dealer.suma(suma_d)}")
            game_on=False
            break
    print(dealer.print_cards())

