from Tkinter import *
import math


class e_calculator:
    def Replace(self):


        self.expression = self.e.get()
        self.newtext = self.expression.replace(self.newdiv, '/')
        self.newtext = self.newtext.replace('x', '*')

    def equals(self):


        self.Replace()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid input')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def squareroot(self):


        self.Replace()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input')
        else:
            self.sqrtval = math.sqrt(self.value)
            self.e.delete(0, END)
            self.e.insert(0, self.sqrtval)

    def square(self):


        self.Replace()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input')
        else:
            self.sqval = math.pow(self.value, 2)
            self.e.delete(0, END)
            self.e.insert(0, self.sqval)

    def clearall(self):

        self.e.delete(0, END)

    def clear1(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi):

        self.e.insert(END, argi)

    def __init__(self, egor_c):

        egor_c.title('Calulator')
        egor_c.geometry()
        self.e = Entry(egor_c)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set()

        self.div = '/'
        self.newdiv = self.div.decode('utf-8')


        Button(egor_c, text="=", width=10, command=lambda: self.equals()).grid(row=4, column=4, columnspan=2)
        Button(egor_c, text='C', width=3, command=lambda: self.clear1()).grid(row=1, column=4  )
        Button(egor_c, text="+", width=3, command=lambda: self.action('+')).grid(row=4, column=3)
        Button(egor_c, text="x", width=3, command=lambda: self.action('x')).grid(row=2, column=3)
        Button(egor_c, text="-", width=3, command=lambda: self.action('-')).grid(row=3, column=3)
        Button(egor_c, text="/", width=3, command=lambda: self.action(self.newdiv)).grid(row=1, column=3)
        Button(egor_c, text="%", width=3, command=lambda: self.action('%')).grid(row=4, column=2)
        Button(egor_c, text="7", width=3, command=lambda: self.action('7')).grid(row=1, column=0)
        Button(egor_c, text="8", width=3, command=lambda: self.action(8)).grid(row=1, column=1)
        Button(egor_c, text="9", width=3, command=lambda: self.action(9)).grid(row=1, column=2)
        Button(egor_c, text="4", width=3, command=lambda: self.action(4)).grid(row=2, column=0)
        Button(egor_c, text="5", width=3, command=lambda: self.action(5)).grid(row=2, column=1)
        Button(egor_c, text="6", width=3, command=lambda: self.action(6)).grid(row=2, column=2)
        Button(egor_c, text="1", width=3, command=lambda: self.action(1)).grid(row=3, column=0)
        Button(egor_c, text="2", width=3, command=lambda: self.action(2)).grid(row=3, column=1)
        Button(egor_c, text="3", width=3, command=lambda: self.action(3)).grid(row=3, column=2)
        Button(egor_c, text="0", width=3, command=lambda: self.action(0)).grid(row=4, column=0)
        Button(egor_c, text=".", width=3, command=lambda: self.action('.')).grid(row=4, column=1)
        Button(egor_c, text="(", width=3, command=lambda: self.action('(')).grid(row=2, column=4)
        Button(egor_c, text=")", width=3, command=lambda: self.action(')')).grid(row=2, column=5)
        Button(egor_c, text="sqrt", width=3, command=lambda: self.squareroot()).grid(row=3, column=4)
        Button(egor_c, text="**", width=3, command=lambda: self.square()).grid(row=3, column=5)



root = Tk()
obj = e_calculator(root)
root.mainloop()