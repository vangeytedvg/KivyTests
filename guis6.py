from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Builder method style 1
Builder.load_file("video6.kv")


# Video 6/54
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


# In this case, the name of the app is indepedent of
# the name in the .kv file!
class DenkaTechApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
