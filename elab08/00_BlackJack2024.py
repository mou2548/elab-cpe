'''
    turtle_BJ.py (aka. version 1.1) brewed by KunToto@MikeLabDotNet [August 2024]
'''
import random, time
#import turtle

class Card():
    ''' Card(): create a card object. To create a deck, try \Card.test_Card()\! '''
    symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"
    def test_Card():
        Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
        Suits = ['D','C','H','S']
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return ' '.join(res)
    #---------------------------------------------------------------------
    def render(self, x, y, color='blue', RENDER=False):
        ''' วาดไพ่ด้วยเต่า '''
        if not RENDER:
            return None
        # Draw border
        pen.penup()
        pen.color(color)
        pen.goto(x+50, y+75)
        xy = ((x+50, y+75), (x+50, y-75), (x-50, y-75), (x-50, y+75))
        pen.begin_fill()
        pen.pendown()
        for pos in xy:
            pen.goto(pos)
        pen.end_fill()
        pen.penup()
        # Draw card info
        if self.name not in ['','O']:
            # Draw suit in the middle
            pen.color('white')
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            # Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
        pen.penup()
    #---------------------------------------------------------------------

class Deck:
    ''' Deck(): สร้างสำรับไพ่ '''
    Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    Suits = ['D','C','H','S']
    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
    def shuffle(self):
        random.shuffle(self.cards)
    def get_card(self):
        return self.cards.pop()
    def set_cards(self, cards):
        self.cards = cards
    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()
    def __repr__(self):
        res = [str(x) for x in self.cards]
        return ' '.join(res)

def preamble(RENDER=False):
    ''' จัดการ environment ในการวาดเต่า '''
    if not RENDER:
        return None
    #--------------------------------------------------------------------------------------
    global wn, pen
    wn, pen = turtle.Screen(), turtle.Turtle()
    wn.bgcolor('black')
    wn.setup(800, 600)
    wn.title('Deck of Cards Simulator by @TokyoEdtech, rebrewed by KunTotoNaMikeLabDotNet')
    pen.speed(0)
    pen.hideturtle()
    #--------------------------------------------------------------------------------------

def test_turtle_deck(RENDER=False):
    ''' ไว้ตรวจสอบเต่าวาดไพ่ ฟังชัน Card.render() '''
    preamble(RENDER)
    # create a deck f card
    deck = Deck()
    # shuffle deck
    deck.reset()
    print(deck)
    # render n cards (back) in a row
    nbOfCards = 5
    start_x = -250
    for x in range(nbOfCards):
        card = Card('', '')
        card.render(start_x + x*125, 175, 'orange', RENDER=True)
    time.sleep(1)
    # re-render n cards in a row
    start_x = -250
    for x in range(nbOfCards):
        card = deck.get_card()
        card.render(start_x + x*125, 175, RENDER=True)
    print('Done..')

def createVirtualDeck(s='K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'):
    dd = s.split()
    res = []
    suit = {'♦':'D','♣':'C','♥':'H','♠':'S'}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck
###
# test_turtle_deck(True)
###
#--------------------------------------------------------------------------------------
# put your additional class or def (aka., utilities) here
# for example,
# class myCards:
#     ''' myCard(): ลิสเก็บไพ่ที่ผู้เล่นถืออยู่ '''
#     pass
#
# def print_result(com, player, com_score, player_score):
#     pass
#--------------------------------------------------------------------------------------

class myCards():
    Values = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':10,'Q':10,'K':10, 'O':0}

    def __init__(self, name="Player", cards=[], hidden=False):
        self.name = name
        self.cards = []
        self.score, self.ace, self.cards_total = 0, 0, 0
        self.busted, self.blackjack = False, False

        if hidden:
            self.cards = [Card('O', cards[0].get_suit())] + cards[1:]
            self.cards_total = len(self.cards)
            for card in cards[1:]:
                self.score += myCards.Values[card.get_name()]
                if card.get_name() == 'A' and self.score + 10 <= 21:
                    self.ace += 1
                    self.score += 10

    def draw(self, card=Deck().get_card()):
        self.cards.append(card)
        self.score += myCards.Values[card.get_name()]
        self.cards_total += 1
        if card.get_name() == 'A' and self.score + 10 <= 21:
            self.ace += 1
            self.score += 10
        if self.score > 21 and self.ace > 0:
            self.score -= 10
            self.ace -= 1

    def checkStatus(self):
        if self.score > 21:
            self.busted = True
        if self.cards_total == 5 and self.score <= 21 or self.score == 21 and self.cards_total == 2:
            self.blackjack = True


def printCards(player, cards, score):
    print(f"{player:>9}:", end=" ")
    for card in cards:
        print(card,end=" ")
    indent = 18 - 3 * len(cards)
    print(f"{'->':>{indent}} {score}")

def checkResult(p1, p2):
    if p1.busted and p2.busted or p1.blackjack and p2.blackjack:
        return 'Draw!'
    elif not p1.busted and p2.busted or p1.blackjack and not p2.blackjack:
        return f'{p1.name} wins.'
    elif p1.busted and not p2.busted or not p1.blackjack and p2.blackjack:
        return f'{p2.name} wins.'
    else:
        if p1.score > p2.score:
            return f'{p1.name} wins.'
        elif p1.score < p2.score:
            return f'{p2.name} wins.'
        else:
            return 'Draw!'

def p1ShouldDraw(p1, p2):
    p1.checkStatus()
    p2.checkStatus()
    p1IsDrawable = not p1.blackjack and p1.cards_total < 5 and p1.score < 21
    p1MustDraw = (p1.score <= 16 or (p2.blackjack and p1.score < 21) or (not p2.busted and p1.score < p2.score))
    return p1IsDrawable and p1MustDraw

def play(player1='Computer', player2='Player', d=None, RENDER=False):
    print('Welcome to MikeLab BlackJack Casino.')
    preamble(RENDER)
    # create a deck of cards
    if d==None:
        deck = Deck()
        deck.reset()
    else:
        #----------------------------- virtual deck
        #d = 'A♦ A♥ 3♥ 4♣ 4♥ 7♣ 5♣ 6♦ A♠'
        deck = createVirtualDeck(d)
    #----------------------
    print(deck) # for DEBUG
    #----------------------
    ###-------------- student code begins here --------------###
    start_cards = 2
    player_draw = 'Y'

    p1 = myCards(name=player1)
    p2 = myCards(name=player2)

    for i in range(start_cards):
        p1.draw(deck.get_card())
        p2.draw(deck.get_card())

    hidden = myCards(name=player1, cards=p1.cards, hidden=True)
    printCards(player1, hidden.cards, hidden.score)
    printCards(player2, p2.cards, p2.score)

    while player_draw == 'Y' and p2.score < 21 and p2.cards_total < 5:
        player_draw = input("Draw another card (y/n): ").upper()
        if player_draw == 'Y':
            p2.draw(deck.get_card())
            printCards(player2, p2.cards, p2.score)
    print('+++++++++++++++++++++++++++++++++')

    while p1ShouldDraw(p1, p2):
        p1.draw(deck.get_card())

    printCards(player1, p1.cards, p1.score)
    printCards(player2, p2.cards, p2.score)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(checkResult(p1, p2))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    ###--------------- student code ends here ---------------###
## main begins here
def testcase01():
    random.seed(2)
    play()
def testcase02():
    random.seed(16)
    play()
def testcase03():
    random.seed(30)
    play()
def testcase04():
    s = 'K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'
    play('Toto', 'Tutu', d=s)

def testcase05():
    s = 'A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase06():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase07():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠'
    play(d=s)
def testcase08():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠'
    play(d=s)
def testcase09():
    s = '5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
#------------------------------------------
q = int(input())
if q==1:
    testcase01()
elif q==2:
    testcase02()
elif q==3:
    testcase03()
elif q==4:
    testcase04()
elif q==5:
    testcase05()
elif q==6:
    testcase06()
elif q==7:
    testcase07()
elif q==8:
    testcase08()
elif q==9:
    testcase09()