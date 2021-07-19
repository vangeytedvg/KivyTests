from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField


class Content(BoxLayout):
    pass


class Example(MDApp):
    dialog = None

    def build(self):
        screen = Builder.load_file("color_theme.kv")
        return screen

    def on_release_alert(self):
        print("KWAAK")

    def on_release_alert2(self):
        print("KWEEKK")

    def closeDialog(self, inst):
        self.dialog.dismiss()


Example().run()
