# coding: utf-8

class City:
    cubeColours = []

    def __init__(self, name, colour):
        self.name = name
        self.hasLab = False
        self.colour = colour
        self.cubes = {}
        self.setCityColours(City.cubeColours)
        self.distance = 999
        self.connectedCities = []

    def getColour(self):
        return self.colour

    def getCountConnections(self):
        return self.connectedCities.__len__()

    def getConnectedCity(self, connection):
        return self.connectedCities[connection - 1]

    def setCityColours(self, cubeColours):
        for colour in cubeColours:
            self.cubes[colour] = 0

    def removeCube(self, colour):
        self.cubes[colour] = self.cubes[colour] - 1

    def addCube(self, colour):
        self.cubes[colour] = self.cubes[colour] + 1

    def getLab(self):
        return self.hasLab

    def buildLab(self):
        if not self.hasLab:
            self.hasLab = True
            return True
        else:
            return False

    def addConnection(self, newConnection):
        self.connectedCities.append(newConnection)

    def getConnections(self):
        return self.connectedCities

    def getName(self):
        return self.name

    def removeAllCubes(self, colour):
        self.cubes[colour] = 0

    def getMaxCubes(self):
        toReturn = 0
        for cubeCount in self.cubes.values():
            if cubeCount > toReturn:
                toReturn = cubeCount
        return toReturn

    def getCubes(self, colour):
        return self.cubes[colour]

    @classmethod
    def setCubeColours(cls, settingsLocation):
        parser = ConfigParser()
        parser.read(settingsLocation)
        cls.cubeColours = parser.get('Colours', 'colours').split(',')

