import kivy

from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        self.btn = Button(text='Hello world', font_size=14)
        self.btn.bind(state=self.callback)
        return self.btn

    def callback(self, instance, value):
        text = str('My button <%s> state is <%s>' % (instance, value))
        print(text)
        self.btn.text = text


if __name__ == "__main__":
    MyApp().run()
