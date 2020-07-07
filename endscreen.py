from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class EndScreen(BoxLayout):
    def __init__(self,**kwargs):
        super(EndScreen,self).__init__(**kwargs)
        self.width = 500
        self.height = 500
        self.orientation = 'horizontal'
        self.size_hint_max_x = 500
        self.size_hint_max_y = 500
        self.label = Label()
        self.label.text = "Congrats"
        self.add_widget(self.label)
        