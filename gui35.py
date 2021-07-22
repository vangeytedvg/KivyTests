from os import SCHED_RESET_ON_FORK, SCHED_RR
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Notice the change here
# Video 3/54
Builder.load_file("video35.kv")

# Video 34/54


class MyLayout(Widget):
    def on_hello(self):
        self.ids.my_label.text = "Clicky Clicked"
        self.ids.my_image.source = "images/login_p.png"

    def on_release(self):
        self.ids.my_image.source = "images/login.png"

class DenkaTechApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
