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

        output_label = TextInput(size_hint_y=0.8, font_size="100sp", readonly=True)

        button_grid = GridLayout(cols=4, size_hint_y=2)


        #button_symbols = ('1', '2', '3', '+',
        #                  '4', '5', '6', '-',
        #                  '7', '8', '9', '÷',
        #                  '0', 'bª', '√', '×',
        #                  '.', 'clr', '=', '<')


        button_1 = Button(text="1", font_size="50sp")
        button_2 = Button(text="2", font_size="50sp")
        button_3 = Button(text="3", font_size="50sp")
        button_plus = Button(text="+", font_size="50sp")
        button_4 = Button(text="4", font_size="50sp")
        button_5 = Button(text="5", font_size="50sp")
        button_6 = Button(text="6", font_size="50sp")
        button_minus = Button(text="-", font_size="50sp")
        button_7 = Button(text="7", font_size="50sp")
        button_8 = Button(text="8", font_size="50sp")
        button_9 = Button(text="9", font_size="50sp")
        button_division = Button(text="÷", font_size="50sp")
        button_0 = Button(text="0", font_size="50sp")
        button_power = Button(text="bª", font_size="50sp")
        button_root = Button(text="√", font_size="50sp")
        button_multiplication = Button(text="×", font_size="50sp")
        button_decimal = Button(text=".", font_size="50sp")
        button_clear = Button(text="clr", font_size="50sp")
        button_equals = Button(text="=", font_size="50sp")
        button_backspace = Button(text="<--", font_size="50sp")

        button_grid.add_widget(button_1)
        button_grid.add_widget(button_2)
        button_grid.add_widget(button_3)
        button_grid.add_widget(button_plus)
        button_grid.add_widget(button_4)
        button_grid.add_widget(button_5)
        button_grid.add_widget(button_6)
        button_grid.add_widget(button_minus)
        button_grid.add_widget(button_7)
        button_grid.add_widget(button_8)
        button_grid.add_widget(button_9)
        button_grid.add_widget(button_division)
        button_grid.add_widget(button_0)
        button_grid.add_widget(button_power)
        button_grid.add_widget(button_root)
        button_grid.add_widget(button_multiplication)
        button_grid.add_widget(button_decimal)
        button_grid.add_widget(button_clear)
        button_grid.add_widget(button_equals)
        button_grid.add_widget(button_backspace)


        #for symbol in button_symbols:
        #    button_grid.add_widget(Button(text=symbol, font_size="50sp"))

        #settings = Button(text="Settings", size_hint_y=0.5, font_size="50sp")

        root.add_widget(output_label)
        root.add_widget(button_grid)
        #root.add_widget(settings)

        return root

if __name__ in ["__main__", "__android__"]:
    sys.exit(App().run())
