from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.button import Button

from ship import Ship


class ShipPicker(BoxLayout):
    def __init__(self,container, **kwargs):
        super(ShipPicker, self).__init__(**kwargs)
        self.width = container.width
        self.height = container.height
        self.size_hint_max_y = 50
        self.size_hint_max_x = 350
        self.orientation = 'horizontal'
        self.sel_orientation_num = 0
        self.sel_orientation_text = "right"
        self.player = None

        self.text_choose = "Choose a ship to place on a board"
        self.label_choose = Label(font_size=15, text=self.text_choose)
        self.label_choose.pos_hint = {'y':0.25}
        self.dropdown = DropDown()
        self.sizes = [2, 3, 4, 6]
        self.remaining = [4,3,2,1]  # [0] = 2squares, [1] = 3squares, [2] = 4squares, [3] = 6 squares
        self.dropdown_buttons = []
        self.selected = 0
        for i in range(4):
            btn = Button(text='■' * self.sizes[i] + ' x%d' % self.remaining[i], size_hint_y=None, height=20)
            btn.id = str(i)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn))
            self.dropdown.add_widget(btn)
        self.mainbutton = Button(text='Choose', size_hint=(None, None), height=20)
        self.mainbutton.pos_hint = {'y':0.5}
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=self.selectShip)
        self.add_widget(self.label_choose)
        self.add_widget(self.mainbutton)

    def refreshDropdown(self):
        self.dropdown.clear_widgets()
        for i in range(4):
            btn = Button(text='■' * self.sizes[i] + ' x%d' % self.remaining[i], size_hint_y=None, height=20)
            btn.id = str(i)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn))
            self.dropdown.add_widget(btn)

    def selectShip(self, instance, buttinstance):
        self.selected = int(buttinstance.id)
        if(self.remaining[self.selected] > 0):
            self.player.setSelected(self.createShip(self.selected))
            self.player.passSelectedToBoard()

    def createShip(self,type):
        ship = Ship()
        ship.setLength(self.sizes[type])
        ship.setOrientation(self.sel_orientation_text)
        ship.setType()
        return ship



    def changeOrientation(self):
        if(self.sel_orientation_num == 3):
            self.sel_orientation_num = 0
        else:
            self.sel_orientation_num += 1
        self.sel_orientation_text = Ship().orientations[self.sel_orientation_num]
        self.player.setSelected(self.createShip(self.selected))
        self.player.board.changeOrientation()


    def setPlayerInstance(self,inst):
        self.player = inst
        self.player.shippicker = self