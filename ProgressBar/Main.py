from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from MyProgressBar import MyProgressBar
from kivy.clock import Clock
import time


from kivy.lang import Builder
Builder.load_file('style.kv')



###########################################################################
## Modified from: https://github.com/kivy/kivy/wiki/Draggable-Scalable-Button
##########################################################################
class Main_app(BoxLayout):
    def __init__(self, **kwargs):
        super(Main_app, self).__init__(**kwargs)

        # Progress bars
        loading_pb = MyProgressBar()
        # Clock.schedule_interval(self.dummy, 1 / 60.)
        # Clock.schedule_once(self.dummy)


    def dummy(self, pb_increment=10):
        # pb_increment = 10

        for i in range(10):
            time.sleep(1)
            self.loading_pb.update_bar(pb_increment)
            print(self.loading_pb.value)
            if self.loading_pb.value >= 100:
                Clock.unschedule(self.dummy)


class Stacked(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (1000, 700)

        return Main_app()

if __name__ == '__main__':
    Stacked().run()
