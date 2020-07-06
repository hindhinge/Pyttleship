from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window

from window import MainWindow

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '800')
Config.write()

class PyttleshipApp(App):
    def build(self):
        mainwindow = MainWindow()
        Window.bind(on_key_down=mainwindow.keypress)
        return mainwindow


if __name__ == '__main__':
    PyttleshipApp().run()