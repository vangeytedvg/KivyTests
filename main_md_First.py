from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.button import MDIconButton

Builder.load_file('tutter.kv')


class MyLayout(Widget):
    pass


class AwesomeApp(MDApp):
    def build(self):

        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
