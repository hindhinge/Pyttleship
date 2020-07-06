from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.label import Label
from boards import PlayerBoard, EnemyBoard
from container import Container
from enemy import Enemy
from marking import BoardMakings
from player import Player
from shippicker import ShipPicker
from spacer import Spacer
from textblock import TextBlock


class MainWindow(Widget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.width = 1000
        self.height = 800
        self.player = Player()
        self.player.setWindow(self)
        self.enemy = Enemy()
        self.enemy.setWindow(self)
        self.turn = 0 #0 = plahyer turn, 1 = enemy turn


        self.container_text = Container("vertical", 1000, 200, 0.25)
        self.textblock = TextBlock(self.container_text)
        self.pos_text = 1 - (self.textblock.height / self.height)
        self.container_text.pos_hint = {'y': self.pos_text, 'x': 0.0}
        self.container_text.add_widget(self.textblock)

        self.container_picker = Container("horizontal", 500, 50, 0.5)
        self.shippicker = ShipPicker(self.container_picker)
        self.shippicker.setPlayerInstance(self.player)
        self.pos_picker = self.pos_text - (self.shippicker.height / self.height)
        self.container_picker.pos_hint = {'y': self.pos_picker, 'x': 0.0}
        self.container_picker.add_widget(self.shippicker)

        self.container_infos = Container("horizontal", 1000, 50, 0.5)
        self.container_infos.pos_hint = {'y': 0.0, 'x': 0.0}
        self.bottom_info = Label(text= 'Place remaining 10 ships.')
        self.container_infos.add_widget(self.bottom_info)

        self.container_markings = Container("horizontal", 1000, 50, 0.75)
        self.markings = BoardMakings(self.container_markings)
        self.markings.createMarkingH()
        self.markings.createMarkingH()
        self.container_markings.pos_hint = {'y': 0.63, 'x': 0.0}
        self.container_markings.add_widget(self.markings)

        self.container_board = Container("horizontal", 1000, 500, 1.0)
        self.container_board.padding = 0
        self.markingv1 = BoardMakings(self.container_board)
        self.markingv2 = BoardMakings(self.container_board)
        self.markingv1.createMarkingV()
        self.markingv2.createMarkingV()
        self.player_board = PlayerBoard()
        self.player.setBoard(self.player_board)
        self.player_board.createTiles()
        self.player_board.setNeighbors()
        self.player_board.setPlayerInstance(self.player)
        self.player_board.setEnemyInstance(self.enemy)
        self.enemy_board = EnemyBoard()
        self.enemy.setBoard(self.enemy_board)
        self.enemy_board.createTiles()
        self.enemy_board.setNeighbors()
        self.enemy_board.setEnemyInstance(self.enemy)
        self.enemy_board.setPlayerInstance(self.player)
        self.container_board.pos_hint = {'y': 0.0, 'x': 0.0}
        self.container_board.add_widget(self.markingv1)
        self.container_board.add_widget(self.player_board)
        self.container_board.add_widget(Spacer())
        self.container_board.add_widget(self.enemy_board)
        self.container_board.add_widget(self.markingv2)

        self.layout = FloatLayout()
        self.layout.size_hint = (None, None)
        self.layout.width = self.width
        self.layout.height = self.height
        self.layout.pos = (0, 0)

        self.layout.add_widget(self.container_text)
        self.layout.add_widget(self.container_picker)
        self.layout.add_widget(self.container_markings)
        self.layout.add_widget(self.container_board)
        self.layout.add_widget(self.container_infos)

        self.add_widget(self.layout)

    def playerPlacementDone(self):
        self.setBottomInfo("Enemy now places his ships.")
        self.enemy.placeShips()

    def enemyPlacementDone(self):
        self.setBottomInfo("Enemy has placed his ships. Your turn to fire !")
        self.takeTurn()
        print("window turn "+ str(self.turn))

    def takeTurn(self):
        if self.turn == 0:
            self.player.takeTurn()
        else:
            self.enemy.takeTurn()

    def changeTurn(self):
        if self.turn == 0:
            self.turn = 1
            self.takeTurn()
        else:
            self.turn = 0
            self.takeTurn()

    def setBottomInfo(self,str):
        setattr(self.bottom_info,'text',str)

    def clicked(self, instance):
        print("click")

    def keypress(self, *args):
        if (args[3] == 'z'):
            self.shippicker.changeOrientation()
        if (args[3] == 'p'):
            self.enemy.placeShips()
        if (args[3] == 'o'):
            self.enemy.clearShips()