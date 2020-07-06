class Ship():
    def __init__(self):
        self.length = 0
        self.position = 0
        self.tiles = []
        self.orientations = ['right','down','left','top']
        self.orientation = "right" #ship rotation based on position [left,right,top,down]
        self.type = 0 #0 - 2 squares, 1 - 3 squares, 2 - 4 squares, 3 - 6 squares

    def setOrientation(self,ori):
        self.orientation = ori

    def setLength(self,len):
        self.length = len

    def setPosition(self,pos):
        self.position = pos

    def getOrientation(self):
        return self.orientation

    def getLength(self):
        return self.length

    def getPosition(self):
        return self.position

    def setTiles(self,tileset):
        self.tiles = tileset

    def setType(self):
        length = self.length
        if length == 2:
            self.type = 0
        if length == 3:
            self.type = 1
        if length == 4:
            self.type = 2
        if length == 6:
            self.type = 3

    def getType(self):
        return self.type
