from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):

    def build(self):
        fullname = "Subhadeep Banerjee"
        return Button(text=f"Hello {fullname}")


if __name__ == "__main__":
    TestApp().run()
