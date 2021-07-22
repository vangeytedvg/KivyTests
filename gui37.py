from kivy.lang import Builder
from kivymd.app import MDApp

# Notice the change here
# Video 3/54
Builder.load_file("video37.kv")


# Video 37/54


class MyLayout(Widget):
    def activated(self, widget, state):
        if state == True:
            self.ids.my_label.text = "On"
        else:
            self.ids.my_label.text = "Off"

class DenkaTechApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
