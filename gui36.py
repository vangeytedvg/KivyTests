from os import SCHED_RESET_ON_FORK, SCHED_RR
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.animation import Animation

# Notice the change here
# Video 3/54
Builder.load_file("video36.kv")


# Video 34/54


class MyLayout(Widget):

    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0, 0, 1, 1),
            duration=.2
        )

        animate += Animation(
            background_color=(1, 0, 1, 1),
            duration=2
        )

        animate += Animation(
            size_hint=(1, 1)
        )

        animate += Animation(
            size_hint=(.3, .3)
        )

        animate.start(widget)


class DenkaTechApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    DenkaTechApp().run()
