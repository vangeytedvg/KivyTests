from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Builder method style 1
Builder.load_file("video8.kv")


# Video 8/54
class MyBoxLayout(Widget):
    pass


class DenkaTechApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
