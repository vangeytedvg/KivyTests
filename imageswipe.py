from kivy.lang import Builder
from kivymd.app import MDApp


# Video 43/54

class DenkaTechApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style="Dark"
        return Builder.load_file('imageswipe.kv')


if __name__ == '__main__':
    DenkaTechApp().run()
