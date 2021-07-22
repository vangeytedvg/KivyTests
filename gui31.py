from os import SCHED_RESET_ON_FORK, SCHED_RR
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# Notice the change here
# Video 31/54
kv = Builder.load_file("video31.kv")


class DenkaTechApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    DenkaTechApp().run()
