import random
import string
from configparser import ConfigParser
import itertools


class PandemicGame:
    def __init__(self):
        self.startingEpidemics = None
        self.outbreakCount = 0
        self.gameOver = False
        self.gameWon = False
        self.diseaseCubes = {}
        self.cityMap = {}
        self.playerDeck = Deck()
        self.infectDeck = Deck()
        self.infectionRate = None
        self.infectionRates = []
        self.epidemicCount = 0
        self.diseases = {}
        self.players = []
        self.turnNumber = None

    def setupGame(self, settingsLocation):
        City.setCubeColours(settingsLocation)
        self.getInfectionRate(settingsLocation)
        self.getNewCities(settingsLocation)
        self.getNewDecks(settingsLocation)
        self.getNewDiseases(settingsLocation)
        self.setStartingEpidemics(settingsLocation)
        for player in self.players:
            player.setLocation(list(self.cityMap.keys())[0])
        AIcontroller.numberAI = 0

    def setStartingEpidemics(self, settingsLocation):
        parser = ConfigParser()
        parser.read(settingsLocation)
        self.startingEpidemics = int(parser.get('Diseases', 'epidemics'))

    def startGame(self):
        self.shuffleDecks()
        self.initalInfectPhase()
        self.drawInitalHands()
        self.addEpidemics()
        pass

    def addEpidemics(self):
        self.playerDeck.addEpidemics(self.startingEpidemics)

    def addPlayer(self, newPlayer):
        newPlayer.setGame(self)
        newPlayer.setController(AIcontroller(newPlayer))
        self.players.append(newPlayer)

    def drawCard(self, playerDrawing):
        drawnCard = self.playerDeck.takeTopCard()
        if drawnCard.getName() == 'Epidemic':
            self.epidemicPhase()
        else:
            playerDrawing.addCard(drawnCard)

    def shuffleDecks(self):
        self.infectDeck.shuffle()
        self.playerDeck.shuffle()

    def hasXCubeCity(self, x):
        for city in self.cityMap.values():
            if city.getMaxCubes() == x:
                return True
        return False

    def getCountXCubeCity(self, x):
        countXCities = 0
        for city in self.cityMap.values():
            if city.getMaxCubes() == x:
                countXCities = countXCities + 1
        return countXCities

    def infectCity(self, city, colour):
        infectCity = self.cityMap.get(city)
        if infectCity.getCubes(colour) < 3:
            infectCity.addCube(colour)
            self.diseaseCubes[colour] = self.diseaseCubes.get(colour) - 1
        else:
            self.outbreak(city, colour)

    def outbreak(self, city, colour):
        outbreakCity = self.cityMap.get(city)
        self.outbreakCount = self.outbreakCount + 1
        for connectedCity in outbreakCity.getConnections():
            self.infectCity(connectedCity.getName(), colour)
        pass

    def initalInfectPhase(self):
        for x in range(1, 4):
            for y in range(1, 4):
                drawnCard = self.infectDeck.takeTopCard()
                self.infectDeck.addDiscard(drawnCard)
                for z in range(0, y):
                    self.infectCity(drawnCard.getName(), drawnCard.getColour())

    def infectCityPhase(self):
        for x in range(0, int(self.infectionRate)):
            drawnCard = self.infectDeck.takeTopCard()
            self.infectDeck.addDiscard(drawnCard)
            infectCity = self.cityMap.get(drawnCard.getName())
            self.infectCity(infectCity.getName(), infectCity.getColour())

    def startTurn(self, player):
        player.setActionCount(4)
        pass

    def epidemicPhase(self):
        drawnCard = self.infectDeck.takeBottomCard()
        self.infectDeck.addDiscard(drawnCard)
        cityEpidemic = self.cityMap.get(drawnCard.getName())
        for x in range(0, 3):
            self.infectCity(cityEpidemic.getName(), cityEpidemic.getColour())
        self.infectDeck.shuffleDiscardToTop()
        self.incrementEpidemicCount()

    def getNewCities(self, settingsLocation):
        parser = ConfigParser()
        parser.read(settingsLocation)
        numberOfCities = int(parser.get('Cities', 'number'))
        for x in range(1, numberOfCities + 1):
            self.cityMap[parser.get('Cities', "city" + str(x))] = City(parser.get('Cities', "city" + str(x)),
                                                                       parser.get('Colours', "city" + str(x)))
        self.makeCities(settingsLocation)

    def newInfectDeck(self, settingsLocation):
        parser = ConfigParser()
        parser.read(settingsLocation)
        numberOfCards = int(parser.get('Cities', 'number'))
        for x in range(1, numberOfCards + 1):
            self.infectDeck.addCard(Card(parser.get('Cities', "city" + str(x)), parser.get('Colours', "city" + str(x))))

    def newPlayerDeck(self, settingsLocation):
        parser = ConfigParser()
        parser.read(settingsLocation)
        numberOfCards = int(parser.get('Cities', 'number'))
        for x in range(1, numberOfCards + 1):
            self.playerDeck.addCard(Card(parser.get('Cities', "city" + str(x)), parser.get('Colours', "city" + str(x))))

    def getNewDecks(self, settingsLocation):
        self.newInfectDeck(settingsLocation)
        self.newPlayerDeck(settingsLocation)

    def getNewDiseases(self, settingsLocation):
        parser = ConfigParser()
        parser.read(settingsLocation)
        numberOfDisease = int(parser.get('Diseases', 'number'))
        for x in range(1, numberOfDisease + 1):
            self.diseases[parser.get('Diseases', 'disease' + str(x))] = Disease(
                parser.get('Diseases', 'disease' + str(x)))
            self.addDiseaseCubes(parser.get('Diseases', 'disease' + str(x)), int(parser.get('Diseases', 'cubes')))

    def addDiseaseCubes(self, colour, number):
        self.diseaseCubes[colour] = number

    def makeCities(self, settingsLocation):
        parser = ConfigParser()
        parser.read(settingsLocation)
        for city in self.cityMap.items():
            connections = parser.get('Connections', city[0])
            usedlist = list(connections.split("\t"))
            for x in usedlist:
                city[1].addConnection(self.cityMap.get(parser.get('Cities', "city" + x)))
        pass

    def setLabDistances(self):
        citiesWithLabs = []
        for city in self.cityMap.values():
            if city.getLab():
                citiesWithLabs.append(city)
        self.setCitiesDistances(citiesWithLabs)

    def setCitiesDistancesNames(self, cityNames):
        cities = []
        for name in cityNames:
            cities.append(self.cityMap.get(name))
        self.setCitiesDistances(cities)

    def setCitiesDistances(self, cities):
        self.resetDistances()
        for city in cities:
            city.setDistance(0)
        self.updateDistances(cities)

    def setCityDistanceName(self, city):
        cityList = [self.cityMap.get(city)]
        self.setCitiesDistances(cityList)

    def setCityDistance(self, city):
        cityList = [city]
        self.setCitiesDistances(cityList)

    def resetDistances(self):
        for city in self.cityMap.values():
            city.setDistance(999)

    def updateDistances(self, startingCities):
        updatedCities = []
        currentDistance = startingCities[0].getDistance()
        for city in startingCities:
            for connectedCity in city.getConnections():
                if connectedCity.getDistance() == 999:
                    updatedCities.append(connectedCity)
                    connectedCity.setDistance(currentDistance + 1)
        if updatedCities.__len__() > 0:
            self.updateDistances(updatedCities)
        pass

    def incrementEpidemicCount(self):
        self.epidemicCount = self.epidemicCount + 1
        self.infectionRate = self.infectionRates[self.epidemicCount]

    def getInfectionRate(self, settingsLocation):
        parser = ConfigParser()
        parser.read(settingsLocation)
        self.infectionRates = list(parser.get('Diseases', 'rate'))
        self.infectionRate = int(self.infectionRates[0])

    def drawInitalHands(self):
        cardsToDraw = 4
        if self.players.__len__() > 4:
            cardsToDraw = 2
        elif self.players.__len__() == 3:
            cardsToDraw = 3
        for player in self.players:
            for x in range(0, cardsToDraw):
                player.addCard(self.playerDeck.takeTopCard())

