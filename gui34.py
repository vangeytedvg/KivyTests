from os import SCHED_RESET_ON_FORK, SCHED_RR
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

# Notice the change here
# Video 32/54
Builder.load_file("video34.kv")

# Video 34/54


class MyLayout(TabbedPanel):
    pass


class DenkaTechApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
