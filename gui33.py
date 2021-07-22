from os import SCHED_RESET_ON_FORK, SCHED_RR
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Notice the change here
# Video 32/54
Builder.load_file("video33.kv")

# Video 33/54


class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text = value


class DenkaTechApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
