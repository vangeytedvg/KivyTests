from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("video14.kv")


# Video 14/54
class MyLayout(Widget):
    def press(self):
        # Create ref vars
        name = self.ids.name_input.text
        # Update the label
        self.ids.name_label.text = f"Hello {name}"
        self.ids.name_input.text = ""


class DenkaTechApp(App):
    def build(self):

        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
