import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


# Video 5/54
class MyGridLayout(Widget):
    # These variables refer to the ones in the .kv file
    # They have no value when the app starts, so we set them
    # to None to begin with
    name = ObjectProperty(None)
    firstname = ObjectProperty(None)

    def press(self):
        # This gets the class variables
        myname = self.name.text
        myfirstname = self.firstname.text
        print(f"Hi {myname} {myfirstname}!")
        # Clear the fields
        self.name.text = ""
        self.firstname.text =""

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
