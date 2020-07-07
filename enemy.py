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
        self.orientations = {0:'down',1:'left',2:'top',3:'right'}
        self.priority_shots = []
        self.forbidden_shots = []
        self.destroyed = 0


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
        output.setOwner(self)
        self.ships.append(output)
        self.printinfo(output)
        return True

    def addToPriority(self,id,ori):
        together = (id,ori)
        self.priority_shots.append(together)

    def takeBlindShot(self):
        valid = 0
        hit = 0
        while valid == 0:
            shot = random.randint(0,99)
            tile = self.board.player.getTileFromBoard(shot)
            if tile.shot == 1 or shot in self.forbidden_shots:
                return 1
            else:
                tile.shot = 1
                if tile.inShip == 1:
                    tile.imageShipHit()
                    ship = tile.getShip()
                    ship.getHit()
                    for i in range(4):
                        ori = self.orientations[i]
                        next_tile = tile.getAdjacent(ori)
                        if next_tile == None:
                            pass
                        else:
                            self.priority_shots.append([next_tile,ori])
                    hit = 1
                else:
                    tile.imageMiss()
                    hit = 0
            valid = 1
            return hit

    def takePriorityShot(self):
        data = self.priority_shots[-1]
        self.priority_shots.remove(data)
        id = data[0].getId()
        ori = data[1]
        tile = self.board.player.getTileFromBoard(id)
        if tile.shot == 1:
            return 1
        else:
            tile.shot = 1
            if tile.inShip == 1:
                tile.imageShipHit()
                ship = tile.getShip()
                ship.getHit()
                if ship.destroyed == 1:
                    self.priority_shots = []
                    ship_tiles = ship.tiles
                    for shiptile in ship_tiles:
                        for i in range(4):
                            next_tile = shiptile.getAdjacent(self.orientations[i])
                            if next_tile != None:
                                self.forbidden_shots.append(next_tile.getId())
                else:
                    if ori == 'left' or ori == 'right':
                        for entry in self.priority_shots:
                            if entry[1] == 'top' or entry[1] == 'down':
                                self.priority_shots.remove(entry)
                    if ori == 'top' or ori == 'down':
                        for entry in self.priority_shots:
                            if entry[1] == 'left' or entry[1] == 'right':
                                self.priority_shots.remove(entry)
                    next_tile = tile.getAdjacent(ori)
                    if next_tile != None:
                        self.priority_shots.append([next_tile,ori])
                hit = 1
            else:
                tile.imageMiss()
                hit = 0
        return hit





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
        if self.phase == 1:
            missed = 0
            while missed == 0:
                self.board.player.checkVictory()
                if len(self.priority_shots) == 0:
                    x = self.takeBlindShot()
                else:
                    x = self.takePriorityShot()
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

    def increaseDestroyed(self):
        self.destroyed += 1

    def checkVictory(self):
        print("destroyed: " + str(self.destroyed) + " avaiulable: " + str(len(self.ships)))
        if self.destroyed == len(self.ships):
            self.window.triggerPlayerVictory()


        

