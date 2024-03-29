import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
kivy.require('2.0.0')
Builder.load_file('MainKV.kv')
from stylesheets.Foo import Foo


class PanelLayout(Screen):
    def __init__(self, **kwargs):
        super(PanelLayout, self).__init__(**kwargs)
        layout = Foo()
        self.ids['first_tab'].add_widget(layout)


class FusionApp(App):
    def build(self):
        return PanelLayout()


if __name__ == '__main__':
    FusionApp().run()