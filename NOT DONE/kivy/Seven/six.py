from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.app import App
import kivy
kivy.require('1.0.7')


class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        print("Mouse Up", touch)
        self.btn.opacity = 1


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    MyApp().run()
