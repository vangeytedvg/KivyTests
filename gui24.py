from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.spelling import Spelling


Builder.load_file("video25.kv")


# Video 24/54
class MyLayout(Widget):
    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1]) * 5)

    def set_orientation(self, direction: str):
        if direction == "V":
            self.ids.sliddy.orientation="vertical"
        elif direction == "H":
            self.ids.sliddy.orientation = "horizontal"


class DenkaTechApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
