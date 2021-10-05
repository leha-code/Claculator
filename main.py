from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import *
import sys, math


class App(App):
    def build(self):
        self.title = "Claculator"
        root = BoxLayout(orientation='vertical')

        self.output_label = TextInput(size_hint_y=0.8, font_size="80sp", readonly=True)

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
        button_backspace = Button(text="<--", font_size="50sp")
        button_equals = Button(text="=", font_size="50sp")
        button_bracket1 = Button(text="(", font_size="50sp")
        button_bracket2 = Button(text=")", font_size="50sp")

        button_1.bind(on_press=lambda instance:
                self.textoutput("1"))
        button_2.bind(on_press=lambda instance:
                self.textoutput("2"))
        button_3.bind(on_press=lambda instance:
                self.textoutput("3"))
        button_plus.bind(on_press=lambda instance:
                self.textoutput("+"))
        button_4.bind(on_press=lambda instance:
                self.textoutput("4"))
        button_5.bind(on_press=lambda instance:
                self.textoutput("5"))
        button_6.bind(on_press=lambda instance:
                self.textoutput("6"))
        button_minus.bind(on_press=lambda instance:
                self.textoutput("-"))
        button_7.bind(on_press=lambda instance:
                self.textoutput("7"))
        button_8.bind(on_press=lambda instance:
                self.textoutput("8"))
        button_9.bind(on_press=lambda instance:
                self.textoutput("9"))
        button_division.bind(on_press=lambda instance:
                self.textoutput("/"))
        button_0.bind(on_press=lambda instance:
                self.textoutput("0"))
        button_power.bind(on_press=lambda instance:
                self.textoutput("**"))
        button_root.bind(on_press=lambda instance:
                self.textoutput("math.sqrt("))
        button_multiplication.bind(on_press=lambda instance:
                self.textoutput("*"))
        button_decimal.bind(on_press=lambda instance:
                self.textoutput("."))
        button_clear.bind(on_press=lambda instance:
                self.clearoutput())
        button_equals.bind(on_press=lambda instance:
                self.validateoutput())
        button_backspace.bind(on_press=lambda instance:
                self.backspace())
        button_bracket1.bind(on_press=lambda instance:
                self.textoutput("("))
        button_bracket2.bind(on_press=lambda instance:
                self.textoutput(")"))



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
        button_grid.add_widget(button_backspace)
        button_grid.add_widget(button_clear)
        button_grid.add_widget(button_equals)
        button_grid.add_widget(button_bracket1)
        button_grid.add_widget(button_bracket2)


        #for symbol in button_symbols:
        #    button_grid.add_widget(Button(text=symbol, font_size="50sp"))

        #settings = Button(text="Settings", size_hint_y=0.5, font_size="50sp")

        root.add_widget(self.output_label)
        root.add_widget(button_grid)
        #root.add_widget(settings)

        return root

    def textoutput(self,str):
        self.output_label.text += str
    def clearoutput(self):
        self.output_label.text = ""
    def validateoutput(self):
        output = self.output_label.text
        exec(f"self.output_label.text=str({output})")

    def backspace(self):
        self.output_label.text = self.output_label.text[:-1]




if __name__ in ["__main__", "__android__"]:
    sys.exit(App().run())
