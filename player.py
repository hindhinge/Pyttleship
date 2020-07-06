class Player():
    def __init__(self):
        self.window = None
        self.board = None
        self.ships = []
        self.selected_ship = None
        self.shippicker = None
        self.phase = 0
        self.turn = 0 #0 its enemy turn, 1 its your turn

    def getTileFromBoard(self,id):
        return self.board.getTile(id)

    def passSelectedToBoard(self):
        if self.selected_ship != None:
            self.board.setSelectedShip(self.selected_ship)

    def getSelected(self):
        if self.selected_ship != None:
            return self.selected_ship

    def getSelectedLength(self):
        if self.selected_ship != None:
            return self.getSelected().getLength()

    def getSelectedOrientation(self):
        if self.selected_ship != None:
            return self.getSelected().getOrientation()

    def appendTileToSelected(self,tile):
        self.selected_ship.tiles.append(tile)

    def clearTileSelected(self):
        for tile in self.selected_ship.tiles:
            tile.imageInactive()
        self.selected_ship.tiles = []

    def addShip(self,inst):
        self.shippicker.remaining[inst.getType()] -= 1
        self.shippicker.refreshDropdown()
        self.ships.append(inst)
        self.printinfo(inst)
        remaining = 0
        for rem in self.shippicker.remaining:
            remaining += rem
        self.window.setBottomInfo("Place remaining " + str(remaining) + " ships.")
        if(remaining == 0):
            self.phase = 1
            self.window.playerPlacementDone()

    def printinfo(self,inst):
        print("Added ship: ")
        print("\tLength: "+ str(inst.getLength()))
        print("\tOrientation: " + inst.getOrientation())
        tiles = []
        for tile in inst.tiles:
            tiles.append(tile.getId())
        print("\tTiles ID: " + str([str(tile) for tile in tiles]))

    def canAdd(self,ship):
        ship_len = ship.getLength()
        for i in range(len(self.shippicker.sizes)):
            if self.shippicker.sizes[i] == ship_len and self.shippicker.remaining[i] > 0:
                return True
        return False

    def getPhase(self):
        return self.phase

    def takeTurn(self):
        self.turn = 1
        print("player turn " + str(self.turn))

    def endTurn(self):
        self.turn = 0
        self.window.changeTurn()

    def setSelected(self,ship):
        self.selected_ship = ship

    def clearSelected(self):
        self.selected_ship = None

    def setBoard(self,instance):
        self.board = instance

    def setWindow(self,instance):
        self.window = instance