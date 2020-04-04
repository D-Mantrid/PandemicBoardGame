# coding: utf-8



class Player:
    def __init__(self, name):
        self.game = None
        self.location = None
        self.actionCount = 0
        self.hand = []
        self.name = name
        self.controller = None

    def get_distance_from_lab(self):
        self.game.set_lab_distances()
        return self.location.getDistance()

    def setController(self, newController):
        self.controller = newController

    def setActionCount(self, x):
        self.actionCount = x

    def getCard(self, cardName):
        for card in self.hand:
            if card.getName() == cardName:
                return card

    def setGame(self, game):
        self.game = game

    def getGame(self):
        return self.game

    def set_location(self, new_location):
        self.location = self.game.cityMap.get(newLocation)

    def checkCharterFlight(self, location, destination):
        if (self.actionCount > 0) & (self.location.getName() == location):
            if self.handContains(location):
                return True
        return False

    def charterFlight(self, location, destination):
        if self.checkCharterFlight(location, destination):
            self.discardCard(location)
            self.setLocation(destination)
            self.actionCount = self.actionCount - 1
            return True
        return False

    def checkDirectFlight(self, location, destination):
        if self.actionCount > 0:
            if self.handContains(destination):
                if self.location.getName() == location:
                    return True
        return False

    def directFlight(self, location, destination):
        if self.checkDirectFlight(location, destination):
            self.discardCard(destination)
            self.setLocation(destination)
            self.actionCount = self.actionCount - 1
            return True
        return False

    def checkBuildLab(self):
        if self.actionCount > 0:
            if self.handContains(self.location.getName()):
                if not self.location.getLab():
                    return True
        return False

    def buildLab(self):
        if self.checkBuildLab():
            self.discardCard(self.location.getName())
            self.location.buildLab()
            self.actionCount = self.actionCount - 1
            return True
        return False

    def checkShuttleFlight(self, location, destination):
        if self.actionCount > 0:
            if location == self.location.getName():
                if self.location.getLab():
                    if self.game.cityMap.get(destination).getLab():
                        return True
        return False

    def shuttleFlight(self, location, destination):
        if self.checkShuttleFlight(location, destination):
            self.setLocation(destination)
            self.actionCount = self.actionCount - 1
            return True
        return False

    def checkTreatDisease(self, colour):
        if self.actionCount > 0:
            if self.location.getCubes(colour) > 0:
                return True
        return False

    def treatDisease(self, colour):
        if self.checkTreatDisease(colour):
            if self.game.diseases.get(colour).getCured():
                self.location.removeAllCubes(colour)
            else:
                self.location.removeCube(colour)
            self.actionCount = self.actionCount - 1
            return True
        return False

    def checkCureDisease(self, card1, card2, card3, card4, card5):
        settry = {self.getCard(card1), self.getCard(card2), self.getCard(card3),
                  self.getCard(card4), self.getCard(card5)}
        if settry.__len__() == 5:
            if self.actionCount > 0:
                if self.handContains(card1) & self.handContains(card2) & self.handContains(card3) & self.handContains(
                        card4) & self.handContains(card5) and self.location.getLab():
                    return True
        return False

    def cureDisease(self, card1, card2, card3, card4, card5):
        if self.checkCureDisease(card1, card2, card3, card4, card5):
            self.game.diseases.get(self.getCard(card1).getColour()).setCured(True)
            self.actionCount = self.actionCount - 1
            return True
        return False

    def checkShareKnowledge(self, card, player):
        if self.actionCount > 0:
            if self.location.getName() == player.getLocation().getName():
                if self.location.getName() == card:
                    return True
        return False

    def shareKnowledge(self, card, player):
        if self.checkShareKnowledge(card, player):
            for heldCard in self.hand:
                if heldCard.getName() == card:
                    player.addCard(heldCard)
                    self.hand.remove(heldCard)
            self.actionCount = self.actionCount - 1
            return True
        return False

    def addCard(self, newCard):
        self.hand.append(newCard)

    def discardCard(self, toDiscard):
        if self.handContains(toDiscard):
            for card in self.hand:
                if card.getName() == toDiscard:
                    self.game.playerDeck.addDiscard(card)
                    self.hand.remove(card)
                    return True
        return False

    def getHandSize(self):
        return self.hand.__len__()

    def handContains(self, cardName):
        for card in self.hand:
            if card.getName() == cardName:
                return True
        return False

    def getController(self):
        return self.controller

    def checkStandardMove(self, location, destination):
        self.game.setCityDistanceName(destination)
        if self.location.getName() == location:
            if self.actionCount > 1:
                if self.location.getDistance() == 1:
                    return True
        return False

    def standardMove(self, location, destination):
        if self.checkStandardMove(location, destination):
            self.setLocation(destination)
            self.actionCount = self.actionCount - 1
            return True
        return False

    def checkLongMove(self, location, destination):
        self.game.setCityDistanceName(destination)
        if self.location.getDistance() < self.actionCount:
            if self.location.getName() == location:
                return True
        return False

    def longMove(self, location, destination):
        if self.checkLongMove(location, destination):
            self.actionCount = self.actionCount - self.location.getDistance()
            self.setLocation(destination)
            return True
        return False

    def getInputs(self):
        pass

