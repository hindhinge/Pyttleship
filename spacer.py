from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

class Spacer(Widget):
    def __init__(self, **kwargs):
        super(Spacer, self).__init__(**kwargs)
        self.width=100
        self.height = 400
        self.size_hint_max_x = self.width
        self.size_hint_max_y = self.height

class Spam(Widget):
    def __init__(self,container, **kwargs):
        super(Spam, self).__init__(**kwargs)
        self.width = 500
        self.height = 500

    def setPosition(self):
        with self.canvas:
            Color(1., 1., 0)
            Rectangle(pos=self.pos, size=(self.width, self.height))