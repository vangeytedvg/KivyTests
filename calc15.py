from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# regex
import re

# Set the size of the app
Window.size = (500, 700)
Builder.load_file("calculator15.kv")


# Video 15-/54
def endswith_number(mystr: str) -> bool:
    """
    Check if the value in the textbox ends with a digit,
    if this is not the case, the calling function can not add another operator!
    :param mystr:
    :return:
    """
    m = re.search(r'\d+$', mystr)
    if m is not None:
        return True
    return False


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        # get what is in the result box
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def add(self):
        prior = self.ids.calc_input.text
        if endswith_number(prior):
            self.ids.calc_input.text = f"{prior}+"

    def substract(self):
        prior = self.ids.calc_input.text
        if endswith_number(prior):
            self.ids.calc_input.text = f"{prior}-"

    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}*"

    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}/"

    def calculate_total(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = str(eval(prior))

    def insert_decimal_dot(self):
        prior = self.ids.calc_input.text
        operators = ["+", "-", "/", "*"]
        for oper in operators:
            if oper in prior[-1] or endswith_number(prior):
                self.ids.calc_input.text = f"{prior}."


class DenkaTechApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
