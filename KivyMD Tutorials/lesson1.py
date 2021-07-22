from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.font_definitions import theme_font_styles


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(
            text="Hello World",
            halign="center",
            theme_text_color="Error",
            font_style="Subtitle2",
        )
        icon_label = MDIcon(
            icon='account-cash',
            halign="center"
        )
        return icon_label


DemoApp().run()
