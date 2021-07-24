from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn = MDFillRoundFlatButton(text="Hahaa")
        screen.add_widget(btn)

        return screen


DemoApp().run()
