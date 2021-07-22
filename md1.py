from kivy.lang import Builder
from kivymd.app import MDApp


# Video 43/54

class DenkaTechApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style="Dark"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('md1.kv')


if __name__ == '__main__':
    DenkaTechApp().run()
