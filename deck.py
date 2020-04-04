# coding: utf-8


class Deck:
    def __init__(self):
        self.cards = []
        self.discard = []

    def takeTopCard(self):
        return self.cards.pop(0)

    def takeBottomCard(self):
        self.cards.reverse()
        toReturn = self.cards.pop(0)
        self.cards.reverse()
        return toReturn

    def addCard(self, newCard):
        self.cards.append(newCard)

    def addDiscard(self, discardedCard):
        self.discard.append(discardedCard)

    def getDiscardCount(self):
        return self.discard.__len__()

    def shuffleDiscardToTop(self):
        random.shuffle(self.discard)
        self.cards.reverse()
        for card in self.discard:
            toUse = self.discard.pop(0)
            self.cards.append(toUse)
        self.cards.reverse()

    def shuffle(self):
        random.shuffle(self.cards)

    def addEpidemics(self, numberEpidemics):
        cardPiles = {}
        for x in range (0, numberEpidemics):
            cardPiles[x] = []
        random.shuffle(self.cards)
        while self.cards.__len__()>0:
            for x in range(0, numberEpidemics):
                cardToAdd = self.cards.pop()
                cardPiles.get(x).append(cardToAdd)
        for x in range(0, numberEpidemics):
            cardPiles.get(x).append(Card("Epidemic", "All"))
            random.shuffle(cardPiles.get(x))
        for x in range(0, numberEpidemics):
            while cardPiles.get(x).__len__() > 0:
                cardToAdd = cardPiles.get(x).pop()
                self.cards.append(cardToAdd)

