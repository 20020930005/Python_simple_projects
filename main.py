from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator ZS")
        master.geometry('357x420+0+0')
        master.config(bg='#000000')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_val = ''  # Initialize entry_val

        # Display entry field
        Entry(master, width=18, bg='#cdb4db', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Buttons
        Button(master, width=11, height=4, text='(', relief='flat', bg='#bde0fe', command=lambda: self.show('(')).place(x=0, y=50)
        Button(master, width=11, height=4, text=')', relief='flat', bg='#bde0fe', command=lambda: self.show(')')).place(x=90, y=50)
        Button(master, width=11, height=4, text='%', relief='flat', bg='#bde0fe', command=lambda: self.show('%')).place(x=180, y=50)
        Button(master, width=11, height=4, text='1', relief='flat', bg='#bde0fe', command=lambda: self.show(1)).place(x=0, y=125)
        Button(master, width=11, height=4, text='2', relief='flat', bg='#bde0fe', command=lambda: self.show(2)).place(x=90, y=125)
        Button(master, width=11, height=4, text='3', relief='flat', bg='#bde0fe', command=lambda: self.show(3)).place(x=180, y=125)
        Button(master, width=11, height=4, text='4', relief='flat', bg='#bde0fe', command=lambda: self.show(4)).place(x=0, y=200)
        Button(master, width=11, height=4, text='5', relief='flat', bg='#bde0fe', command=lambda: self.show(5)).place(x=90, y=200)
        Button(master, width=11, height=4, text='6', relief='flat', bg='#bde0fe', command=lambda: self.show(6)).place(x=180, y=200)
        Button(master, width=11, height=4, text='7', relief='flat', bg='#bde0fe', command=lambda: self.show(7)).place(x=0, y=275)
        Button(master, width=11, height=4, text='8', relief='flat', bg='#bde0fe', command=lambda: self.show(8)).place(x=180, y=275)
        Button(master, width=11, height=4, text='9', relief='flat', bg='#bde0fe', command=lambda: self.show(9)).place(x=90, y=275)
        Button(master, width=11, height=4, text='0', relief='flat', bg='#bde0fe', command=lambda: self.show(0)).place(x=90, y=350)
        Button(master, width=11, height=4, text='.', relief='flat', bg='#bde0fe', command=lambda: self.show('.')).place(x=180, y=350)

        Button(master, width=11, height=4, text='+', relief='flat', bg='#bde0fe', command=lambda: self.show('+')).place(x=270, y=275)
        Button(master, width=11, height=4, text='-', relief='flat', bg='#bde0fe', command=lambda: self.show('-')).place(x=270, y=200)
        Button(master, width=11, height=4, text='/', relief='flat', bg='#bde0fe', command=lambda: self.show('/')).place(x=270, y=50)
        Button(master, width=11, height=4, text='*', relief='flat', bg='#bde0fe', command=lambda: self.show('*')).place(x=270, y=125)
        Button(master, width=11, height=4, text='=', relief='flat', bg='#cdb4db', command=self.solve).place(x=270, y=350)
        Button(master, width=11, height=4, text='C', relief='flat', bg='#cdb4db', command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.entry_val += str(value)
        self.equation.set(self.entry_val)

    def clear(self):
        self.entry_val = ''
        self.equation.set(self.entry_val)

    def solve(self):
        try:
            result = eval(self.entry_val)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()
