from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '800')
Config.write()

class MainWindow(Widget):
    def __init__(self,**kwargs):
        super(MainWindow,self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.size = (1000,800)
        ###layout info
        layout_info = BoxLayout(orientation = 'vertical')
        layout_info.size_hint = (1.0,0.375)
        label1 = Label(font_size = 30,text="Welcome to Pyttleships")
        label2 = Label(font_size=20, text="Welcome to Pyttleships")
        label3 = Label(font_size=10, text="Welcome to Pyttleships")
        layout_info.add_widget(label1)
        layout_info.add_widget(label2)
        layout_info.add_widget(label3)
        layout.add_widget(layout_info)

        ###layoutboard
        layout_board = BoxLayout(orientation = 'horizontal')
        layout_board.size = (1000,500)
        board1 = Board()
        board1.setPosition(0,0)
        board2 = Board()
        board2.setPosition(500, 0)
        layout_board.add_widget(board1)
        layout_board.add_widget(board2)
        layout.add_widget(layout_board)

        self.add_widget(layout)




class Board(GridLayout):
    def __init__(self,**kwargs):
        super(Board,self).__init__(**kwargs)
        self.width = 500
        self.height = 500
        self.cols = 10
        self.rows = 10
        self.row_force_default = True
        self.row_default_height = 40
        self.col_force_default = True
        self.col_default_width = 40
        self.spacing = 5
        for i in range (100):
            self.add_widget(Button(text=''))

    def setPosition(self,x,y):
        self.pos = (x,y)
        with self.canvas:
            Color(1., 1., 0)
            Rectangle(pos = self.pos,size=(self.width,self.height))




class PyttleshipApp(App):
    def build(self):
        mainwindow = MainWindow()
        return mainwindow


if __name__ == '__main__':
    PyttleshipApp().run()