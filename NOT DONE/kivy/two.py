from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 6
        self.add_widget(Label(text="First Name: "))
        self.fname = TextInput(multiline=False)
        self.add_widget(self.fname)

        self.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False)
        self.add_widget(self.lname)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)


class TestApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    TestApp().run()
