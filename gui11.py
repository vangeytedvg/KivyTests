from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# Second way to change window background color
from kivy.core.window import Window





Builder.load_file("video11.kv")


# Video 9/54
class MyBoxLayout(Widget):
    pass


class DenkaTechApp(App):
    def build(self):
        # Second way, comment for first method (kv)
        # If kv settings remain, they override the code below!
        Window.clearcolor = (240/255, 141/255, 70/255,1)
        return MyBoxLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
