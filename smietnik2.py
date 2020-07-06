from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.button import Button

from functools import partial

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '800')
Config.write()


class MainWindow(Widget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.width = 1000
        self.height = 800

        self.layout_main = BoxLayout()
        self.layout_main.orientation = 'vertical'
        self.layout_main.width = self.width
        self.layout_main.height = self.height
        self.layout_main.spacing = 0

        self.textblock = TextBlock()
        self.layout_main.add_widget(self.textblock)

        self.shippicker = ShipPicker()
        self.layout_main.add_widget(self.shippicker)

        self.add_widget(self.layout_main)


class TextBlock(BoxLayout):
    def __init__(self, **kwargs):
        super(TextBlock, self).__init__(**kwargs)
        self.width = 1000
        self.height = 150
        self.orientation = 'vertical'
        self.text_welcome = "Welcome to Pyttleships !"
        self.text_first_stage = "Place all of your ships on the board to the right.\nThis board will keep track of your enemy shots and your remaining ships."
        self.text_second_stage = "After you finish placing your ships, enemy will do the same."
        self.text_third_stage = "Now, that enemy has placed his ships, its time to take turns at shots to see who will sink all the enemy ships.\nClick on the left board to take a shot."
        self.text_instructions = "Left click - take a shot/place ship\nZ - rotate ship during placement\n"
        self.text_stage = self.text_first_stage
        self.placeLabels()

    def placeLabels(self):
        label_welcome = Label(font_size=40, halign='center', text=self.text_welcome)
        label_welcome.pos = (self.pos)
        label_stage = Label(font_size=20, halign='center', text=self.text_stage)
        label_stage.pos = (self.pos)
        label_instruction = Label(font_size=20, halign='left', text=self.text_instructions)
        self.add_widget(label_welcome)
        self.add_widget(label_stage)
        self.add_widget(label_instruction)


class ShipPicker(Widget):
    def __init__(self, **kwargs):
        super(ShipPicker, self).__init__(**kwargs)
        self.height = 50
        self.width = 1000
        self.layout = BoxLayout()
        self.layout.width = self.width
        self.layout.height = self.height
        self.layout.orientation = 'horizontal'
        self.text_choose = "Choose a ship to place on a board"
        self.label_choose = Label(font_size=15, text=self.text_choose)
        self.dropdown = DropDown()
        self.sizes = [2, 3, 4, 6]
        self.remaining = [4, 3, 2, 1]  # [0] = 2squares, [1] = 3squares, [2] = 4squares, [3] = 6 squares
        self.dropdown_buttons = []
        self.selected = 0
        for i in range(4):
            btn = Button(text='■' * self.sizes[i] + ' x%d' % self.remaining[i], size_hint_y=None, height=20)
            btn.id = str(i)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn))
            self.dropdown.add_widget(btn)
        self.mainbutton = Button(text='Hello', size_hint=(None, None), height=20)
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=self.selectShip)
        self.layout.add_widget(self.label_choose)
        self.layout.add_widget(self.mainbutton)
        self.add_widget(self.layout)

    def selectShip(self, instance, buttinstance):
        setattr(self.mainbutton, 'text', buttinstance.text)
        print(buttinstance.id)


class BoardMakings(BoxLayout):
    def __init__(self, **kwargs):
        super(BoardMakings, self).__init__(**kwargs)
        self.width = 1000
        self.height = 50
        self.orientation = 'horizontal'
        self.labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.add_widget(self.createMarking())
        self.add_widget(self.createMarking())

    def createMarking(self):
        layout = BoxLayout()
        layout.height = self.height
        layout.width = self.width / 2
        layout.orientation = 'horizontal'
        layout.spacing = 2
        layout.padding = (25, 0, 25, 0)
        for i in range(10):
            label = Label(font_size=10, text=self.labels[i])
            layout.add_widget(label)
        return layout


class BoardBlock(BoxLayout):
    def __init__(self, **kwargs):
        super(BoardBlock, self).__init__(**kwargs)
        self.height = 500
        self.width = 1000
        self.orientation = 'horizontal'


class Board(GridLayout):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.width = 500
        self.height = 500
        self.cols = 10
        self.rows = 10
        self.row_force_default = True
        self.row_default_height = 40
        self.col_force_default = True
        self.col_default_width = 40
        self.padding = 0
        self.spacing = 5
        for i in range(100):
            self.add_widget(Button(text=''))

    def setPosition(self, x, y):
        self.pos = (x, y)
        with self.canvas:
            Color(1., 1., 0)
            Rectangle(pos=self.pos, size=(self.width, self.height))


class PyttleshipApp(App):
    def build(self):
        mainwindow = MainWindow()
        textblock = TextBlock()
        return mainwindow


if __name__ == '__main__':
    PyttleshipApp().run()