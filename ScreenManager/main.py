import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
kivy.require('2.0.0')
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Builder.load_file('MainKV.kv')


class WindowManager(ScreenManager):
    pass

class DirectoryScreen(Screen):
    def __init__(self, **kwargs):
        super(DirectoryScreen, self).__init__(**kwargs)
        self.init_widget()

    def init_widget(self, *args):
        fc = self.ids['filechooser']
        fc.bind(on_entry_added=self.update_file_list_entry)
        fc.bind(on_subentry_to_entry=self.update_file_list_entry)

    def update_file_list_entry(self, file_chooser, file_list_entry, *args):
        file_list_entry.children[0].color = (0.0, 0.0, 0.0, 1.0)  # File Names
        file_list_entry.children[1].color = (0.0, 0.0, 0.0, 1.0)  # Dir Names`

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

screen_manager = ScreenManager()
screen_manager.add_widget(MainWindow(name="main"))
screen_manager.add_widget(DirectoryScreen(name="directory_screen"))

class FusionApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return screen_manager


if __name__ == '__main__':
    FusionApp().run()