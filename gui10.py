from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# This app shows the usage of widget inheritance

Builder.load_file("video10.kv")


# Video 9/54
class MyBoxLayout(Widget):
    pass


class DenkaTechApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
