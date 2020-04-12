import kivy

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

import os
import numpy as np

class KivyApp(App):
    def build(self):
        layout = AnchorLayout(
            anchor_x='right',
            anchor_y='center'
        )

        btn1 = Button(text="Button 1")
        btn2 = Button(text="Button 2")
        btn3 = Button(text="Button 3")
        btn4 = Button(text="Button 4")
        btn5 = Button(text="Button 5")

        layout.add_widget(btn1)

        layout.anchor_x = 'center'
        layout.anchor_y = 'center'
        layout.add_widget(btn2)
        
        layout.anchor_x = 'left'
        layout.anchor_y = 'center'
        layout.add_widget(btn3)
        
        layout.anchor_x = 'right'
        layout.anchor_y = 'bottom'
        layout.add_widget(btn4)
        
        layout.anchor_x = 'center'
        layout.anchor_y = 'bottom'
        layout.add_widget(btn5)
        return layout

if __name__ == "__main__":
    KivyApp().run()
