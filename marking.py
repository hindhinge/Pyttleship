from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class BoardMakings(BoxLayout):
    def __init__(self,container, **kwargs):
        super(BoardMakings, self).__init__(**kwargs)
        self.container = container
        self.width = container.width
        self.height = container.height
        self.orientation = 'horizontal'
        self.labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def createMarkingH(self):
        layout = BoxLayout()
        layout.height = self.height
        layout.width = self.width / 2
        layout.orientation = 'horizontal'
        layout.spacing = 0
        layout.padding = (50, 0, 50, 0)
        for i in range(10):
            label = Label(font_size=15, text=self.labels[i],size_hint = (None,None), size = (40,40), valign = 'center', halign = 'center')
            layout.add_widget(label)
        self.add_widget(layout)

    def createMarkingV(self):
        self.height = 400
        self.width = 50
        self.size_hint_max_x = self.width
        layout = BoxLayout()
        layout.height = self.height
        layout.width = self.width
        layout.size_hint_max_x = self.size_hint_max_x
        layout.orientation = 'vertical'
        layout.padding = (0,0,0,100)
        layout.spacing = 0
        for i in range(10):
            label = Label(font_size=15, text=str(i+1), size_hint = (None,None), size = (40,40), valign = 'center', halign = 'center')
            layout.add_widget(label)
        self.add_widget(layout)