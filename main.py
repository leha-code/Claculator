from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import *
import sys


class App(App):
    def build(self):
        self.title = "Claculator"
        root = BoxLayout(orientation='vertical')

        output_label = TextInput(size_hint_y=0.8, font_size="100sp")

        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '÷',
                          '0', 'bª', '√', '×',
                          '.', 'clr', '=', '<')

        button_grid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol, font_size="50sp"))

        root.add_widget(output_label)
        root.add_widget(button_grid)

        return root

if __name__ in ["__main__", "__android__"]:
    sys.exit(App().run())
