from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty

Builder.load_file('style.kv')
from kivy.storage.jsonstore import JsonStore

store = JsonStore('nms.json')

class Main_app(BoxLayout):
    def __init__(self, **kwargs):
        super(Main_app, self).__init__(**kwargs)
        self.name_list_lbl = StringProperty(self.get_names())


    def add_name(self, name):
        store.put(name, name='Mathieu', org='kivy')

    def get_names(self):
        # self.ids.modalities_lbl.text = self.ids.modalities_lbl.text + mod_key + '\n\n'
        name_list = ''
        for person in store.keys():
            name_list = name_list + '\n'+person
        self.ids.name_list_lbl.text = name_list
        print(self.name_list_lbl)

class Stacked(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1000, 700)

        return Main_app()


if __name__ == '__main__':
    Stacked().run()
