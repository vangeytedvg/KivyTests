from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file("video29.kv")


# Video 29/54
class MyLayout(Widget):
    topp = []
    strs = ""

    # Adapted this to my way
    def checkbox_click(self, instance, value, topping):
        if value:
            self.topp.append(topping)
            strs = ', '.join([str(item) for item in self.topp])
        else:
            self.topp.remove(topping)
            strs = ', '.join([str(item) for item in self.topp])
        self.ids.output_label.text = f"{strs}"


class DenkaTechApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
