from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.graphics.transformation import Matrix

from kivy.lang import Builder
Builder.load_file('MyButton.kv')


class Main_app(BoxLayout):
    def btn_push(self):
        print('PUSHED!')

class Stacked(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1000, 700)

        return Main_app()

if __name__ == '__main__':
    Stacked().run()