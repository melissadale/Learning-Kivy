import kivy
from kivy.uix.gridlayout import GridLayout
kivy.require('2.0.0')
from kivy.lang import Builder
Builder.load_file('stylesheets/PanelOne.kv')



class Foo(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def hello(self):
        print('HELLO WORLD')