import random
from ship import Ship

class Enemy():
    def __init__(self):
        self.ships = []
        self.board = None
        self.phase = 0
        self.window = None
        self.sizes = [2,3,4,6]
        self.remaining = [4,3,2,1]
        self.placed = 0
        self.orientations = {0:'right',1:'down',2:'left',3:'top'}
        self.priority_shots = []


    def setBoard(self,instance):
        self.board = instance

    def setWindow(self,instance):
        self.window = instance

    def placeShips(self):
        for i in range(3,-1,-1):
            while self.remaining[i] > 0:
                x = self.placeShip(self.sizes[i])
                if x == True:
                    self.remaining[i] -= 1
        self.phase = 1
        self.window.enemyPlacementDone()

    def placeShip(self,length):
        output = Ship()
        random.seed(a = None)
        length = length
        ori = self.getRandomOrientation()
        position = random.randint(0,99)
        tile = self.board.tiles[position]
        tiles = []
        if tile.invalid == 1 or tile.inShip == 1:
            return False
        for i in range(length):
            if tile == None or tile.inShip == 1 or tile.invalid == 1:
                return False
            else:
                tiles.append(tile)
                tile = tile.getAdjacent(ori)
        for tile in tiles:
            tile.inShip = 1
            tile.setShip(output)
            tile.imageShip()
            neighbourhood = []
            neighbourhood.append(tile.getAdjacent('right'))
            neighbourhood.append(tile.getAdjacent('left'))
            neighbourhood.append(tile.getAdjacent('top'))
            neighbourhood.append(tile.getAdjacent('down'))
            for tile in neighbourhood:
                if tile != None:
                    tile.setInvalid()
        output.setLength(length)
        output.setOrientation(ori)
        output.setPosition(position)
        output.setTiles(tiles)
        self.ships.append(output)
        self.printinfo(output)
        return True


    def takeBlindShot(self):
        valid = 0
        hit = 0
        while valid == 0:
            shot = random.randint(0,99)
            tile = self.board.player.getTileFromBoard(shot)
            if tile.shot == 1:
                pass
            else:
                tile.shot = 1
                if tile.inShip == 1:
                    tile.imageShipHit()
                    ship = tile.getShip()
                    ship.getHit()
                    neigh = []
                    neigh.append(tile.getAdjacent('right'))
                    neigh.append(tile.getAdjacent('top'))
                    neigh.append(tile.getAdjacent('left'))
                    neigh.append(tile.getAdjacent('down'))
                    for tile in neigh:
                        if tile != None:
                            self.priority_shots.append(tile.getId())

                    hit = 1
                else:
                    tile.imageMiss()
                    hit = 0
            print(self.priority_shots)
            valid = 1
            return hit

    def takePriorityShot(self):
        pass



    def getRandomLength(self):
        found = 0
        while found == 0:
            roll = random.randint(0,3)
            length = self.sizes[roll]
            if self.remaining[roll] > 0:
                found = 1
                return length
            else:
                pass

    def printinfo(self,inst):
        print("Added ship: ")
        print("\tLength: "+ str(inst.getLength()))
        print("\tOrientation: " + inst.getOrientation())
        tiles = []
        for tile in inst.tiles:
            tiles.append(tile.getId())
        print("\tTiles ID: " + str([str(tile) for tile in tiles]))

    def getRandomOrientation(self):
        roll = random.randint(0,3)
        return self.orientations[roll]

    def takeTurn(self):
        missed = 0
        while missed == 0:
            # if len(self.priority_shots) == 0:
            #     x = self.takeBlindShot()
            # else:
            #     x = self.takePriorityShot()
            x = self.takeBlindShot()
            if x:
                missed = 0
            else:
                missed = 1
        self.window.changeTurn()

    def clearShips(self):
        for ship in self.ships:
            for tile in ship.tiles:
                tile.invalid = 0
                tile.inShip = 0
                tile.imageInactive()
                neighbourhood = []
                neighbourhood.append(tile.getAdjacent('right'))
                neighbourhood.append(tile.getAdjacent('left'))
                neighbourhood.append(tile.getAdjacent('top'))
                neighbourhood.append(tile.getAdjacent('down'))
                for tile in neighbourhood:
                    if tile != None:
                        tile.invalid = 0
        self.ships = []
        self.remaining = [4,3,2,1]


        

