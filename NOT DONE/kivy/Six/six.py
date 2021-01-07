from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
import kivy
kivy.require('1.0.7')


class MyApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyApp().run()
