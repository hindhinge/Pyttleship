from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout

class Container(BoxLayout):
    def __init__(self,orientation,width,height,color,**kwargs):
        super(Container,self).__init__(**kwargs)
        self.orientation = orientation
        self.width = width
        self.height = height
        self.size_hint_max_y = height
        self.color = color

    def setPos(self):
        print(self.pos)
        with self.canvas:
            Color (self.color, 0, 0)
            Rectangle(pos=self.pos,size = (self.width,self.height))