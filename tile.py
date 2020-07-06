from kivy.uix.button import Button
from kivy.core.window import Window

class Tile(Button):
    def __init__(self,board, **kwargs):
        self.width = 40
        self.height = 40
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        self.identity = 0
        self.adjacent = {'left':None,'right':None,'top':None,'down':None}
        self.bg_normal = 'tile_inactive.png'
        self.bg_highlight = 'tile_selection.png'
        self.bg_ship = 'tile_ship.png'
        self.bg_ship_hit = 'tile_ship_hit.png'
        self.bg_miss = 'tile_miss.png'
        self.bg_hit = 'tile_hit.png'
        self.background_normal = self.bg_normal
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(Tile, self).__init__(**kwargs)
        self.hovered = 0
        self.border_point = 0
        self.size_hint = (None,None)
        self.size = (40,40)
        self.board = board
        self.lastpos = (0,0)
        self.inShip = 0
        self.invalid = 0
        self.shot = 0
        self.ship = None

    def setId(self, id):
        self.identity = id

    def getId(self):
        return self.identity

    def setAdjacent(self,adj):
        self.adjacent = adj

    def getAdjacent(self,dir):
        return self.adjacent[dir]

    def setInvalid(self):
        self.invalid = 1

    def printAdjacent(self):
        print("Tile id: " + str(self.getId()))
        neigh = []
        ids = []
        for dict in self.adjacent:
            neigh.append(self.adjacent[dict])
        for tile in neigh:
            if tile == None:
                ids.append("None")
            else:
                ids.append(str(tile.getId()))
        for id in ids:
            print(id)

    def imageHighlighted(self):
        self.background_normal = self.bg_highlight
    def imageInactive(self):
        self.background_normal = self.bg_normal
    def imageShip(self):
        self.background_normal = self.bg_ship
    def imageShipHit(self):
        self.background_normal = self.bg_ship_hit
    def imageMiss(self):
        self.background_normal = self.bg_miss
    def imageHit(self):
        self.background_normal = self.bg_hit

    def setShip(self,instance):
        self.ship = instance

    def getShip(self):
        return self.ship

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        if not inside:
            self.dispatch('on_leave')

    def on_enter(self):
        self.board.highlightTile(self.getId())

    def on_leave(self):
        pass

    def on_click(self,instance):
        self.board.clickTile()