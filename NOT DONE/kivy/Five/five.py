from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.app import App
import kivy
kivy.require('1.0.7')


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print(f"Name: {self.name.text} Email: {self.email.text}")
        self.name.text = " "
        self.email.text = " "


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
