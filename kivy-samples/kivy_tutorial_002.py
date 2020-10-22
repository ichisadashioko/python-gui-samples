from kivy.app import App
from kivy.uix.widget import Widget

class TouchInput(Widget):
    def on_touch_down(self, touch):
        print(touch)

class SimpleKivy(App):
    def build(self):
        return TouchInput()

if __name__ == "__main__":
    SimpleKivy().run()
