from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("video12.kv")


# Video 12/54
class MyBoxLayout(Widget):
    pass


class DenkaTechApp(App):
    def build(self):

        return MyBoxLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
