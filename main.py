"""
    Example from the Kivy Tutorial at : https://kivy.org/doc/stable/tutorials/pong.html
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector


class PongGame(Widget):
    pass


class PongBall(Widget):
    # velocity of the ball on the x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    # referencelist property
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    # TODO: Continue HERE


# Important, this is the name of the app, so the .kv file must math the
# same name, in this case pong.kv
class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
