from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.fname = TextInput(multiline=False)
        self.inside.add_widget(self.fname)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit",
                             font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        # print("Pressed")
        firstname = self.fname.text
        lastanme = self.lname.text
        emailid = self.email.text
        print(
            f"First Name: {firstname}\nLast Name: {lastanme}\nEmail: {emailid}")
        self.fname.text = " "
        self.lname.text = " "
        self.email.text = " "


class TestApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    TestApp().run()
