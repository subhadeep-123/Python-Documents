from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.app import App
import kivy
kivy.require('1.0.7')


class Touch(Widget):

    def __init__(self, **kwargs):ṇ
        super(Touch, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 0, 0.5, mode='rgba')
            Line(points=(20, 30, 400, 500, 60, 500))
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))
            # Color(1, 1, 0, 0.5, mode='rgba')
            # self.rect = Rectangle(pos=(200, 300), size=(100, 50))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Move", touch)


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    MyApp().run()
