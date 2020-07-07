from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TextBlock(BoxLayout):
    def __init__(self,container, **kwargs):
        super(TextBlock, self).__init__(**kwargs)
        self.width = container.width
        self.height = container.height
        self.size_hint_max_y = 200
        self.orientation = 'vertical'
        self.text_welcome = "Welcome to Pyttleships !"
        self.text_first_stage = "Place all of your ships on the board to the left.\nThis board will keep track of enemy shots and your remaining ships.\nAfter you place all your ships click on board to the right to take shot."
        self.text_second_stage = "After you finish placing your ships, enemy will do the same."
        self.text_third_stage = "Now, that enemy has placed his ships, its time to take turns at shots to see who will sink all the enemy ships.\nClick on the left board to take a shot."
        self.text_instructions = "Left click - take a shot/place ship\nZ - rotate ship during placement\n"
        self.text_stage = self.text_first_stage
        self.placeLabels()

    def placeLabels(self):
        label_welcome = Label(font_size=20, halign='center', text=self.text_welcome, pos_hint = {'top':1.0})
        label_stage = Label(font_size=15, halign='center', text=self.text_stage)
        label_instruction = Label(font_size=15, halign='left', text=self.text_instructions)
        self.add_widget(label_welcome)
        self.add_widget(label_stage)
        self.add_widget(label_instruction)