from kivy.uix.gridlayout import GridLayout

from ship import Ship
from tile import Tile

class Board(GridLayout):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.height = 400
        self.width = 400
        self.size_hint_max_x = self.width
        self.size_hint_max_y = self.height
        self.cols = 10
        self.rows = 10
        self.spacing = 0
        self.tiles = []

    def createTiles(self):
        for i in range(100):
            tile = Tile(self)
            tile.setId(i)
            tile.text = str(i)
            tile.bind(on_press = self.clickTile)
            self.tiles.append(tile)
            self.add_widget(tile)

    def getNeighbors(self,id):
        adjs = {'left':None,'right':None,'top':None,'down':None}
        if str(id)[-1] == str(0):
            adjs['left'] = None
        else:
            adjs['left'] = self.tiles[id-1]

        if str(id)[-1] == str(9):
            adjs['right'] = None
        else:
            adjs['right'] = self.tiles[id + 1]

        if len(str(id)) == 1:
            adjs['top'] = None
        else:
            adjs['top']  = self.tiles[id - 10]

        if len(str(id)) == 2 and str(id)[0] == str(9):
            adjs['down'] = None
        else:
            adjs['down'] = self.tiles[id + 10]
            pass
        return adjs


    def setNeighbors(self):
        for tile in self.tiles:
            tile.setAdjacent(self.getNeighbors(tile.getId()))

    def clickTile(self,instance):
        pass

class PlayerBoard(Board):
    def __init__(self, **kwargs):
        super(PlayerBoard, self).__init__(**kwargs)
        self.player = None
        self.enemy = None
        self.valid_location = 0
        self.selectedShip = None
        self.selectedShipLen = 0
        self.selectedShipOri = ''
        self.highlighted = []
        self.ready = 1

    def setSelectedShip(self,inst):
        self.selectedShip = inst
        self.selectedShipLen = self.selectedShip.getLength()
        self.selectedShipOri = self.selectedShip.getOrientation()

    def setPlayerInstance(self,inst):
        self.player = inst

    def setEnemyInstance(self,inst):
        self.enemy = inst

    def getTile(self,id):
        return self.tiles[id]

    def highlightTile(self,id):
        if self.ready == 1 and self.player.getPhase() == 0:
            self.ready = 0
            for tile in self.highlighted:
                if tile.inShip == 0 and tile.invalid == 0:
                    tile.imageInactive()
            self.highlighted = []
            tile = self.tiles[id]
            for i in range(self.selectedShipLen):
                if tile == None or tile.inShip == 1 or tile.invalid == 1:
                    self.valid_location = 0
                    break
                else:
                    tile.imageHighlighted()
                    self.highlighted.append(tile)
                    self.valid_location = 1
                    tile = tile.getAdjacent(self.selectedShipOri)
            self.ready = 1
        else:
            pass

    def changeOrientation(self):
        self.player.passSelectedToBoard()

    def clickTile(self,instance):
        if self.valid_location == 1 and self.player.canAdd(self.selectedShip) and self.player.getPhase() == 0:
            for tile in self.highlighted:
                tile.inShip = 1
                tile.setShip(self.selectedShip)
                tile.imageShip()
                neighbourhood = []
                neighbourhood.append(tile.getAdjacent('right'))
                neighbourhood.append(tile.getAdjacent('left'))
                neighbourhood.append(tile.getAdjacent('top'))
                neighbourhood.append(tile.getAdjacent('down'))
                for tile in neighbourhood:
                    if tile != None:
                        tile.setInvalid()
            self.selectedShip.setTiles(self.highlighted)
            self.player.addShip(self.selectedShip)







class EnemyBoard(Board):
    def __init__(self, **kwargs):
        super(EnemyBoard, self).__init__(**kwargs)
        self.enemy = None
        self.player = None

    def setPlayerInstance(self,inst):
        self.player = inst

    def setEnemyInstance(self,inst):
        self.enemy = inst

    def highlightTile(self,id):
        pass

    def clearHighlighted(self):
        pass

    def getTile(self,id):
        return self.tiles[id]

    def clickTile(self, instance):
        if self.player.turn and self.player.phase == 1:
            id = instance.getId()
            tile = self.getTile(id)
            if tile.shot == 1:
                return
            else:
                tile.shot = 1
                if tile.inShip == 1:
                    tile.imageHit()
                    ship = tile.getShip()
                    ship.getHit()
                    self.enemy.checkVictory()
                else:
                    tile.imageMiss()
                    self.player.endTurn()


