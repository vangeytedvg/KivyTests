from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    """ Main entry point

    Args:
        MDApp 
    """
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('color_theme.kv')


MainApp().run()