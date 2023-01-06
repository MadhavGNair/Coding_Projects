import tkinter as tk
import tkinter.messagebox as tkm


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.equation = tk.Entry(master, width=36, borderwidth=5, font=('Arial', 12))
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.createButton()

    def createButton(self):
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton('+')
        b_sub = self.addButton('-')
        b_mult = self.addButton('*')
        b_div = self.addButton('/')
        b_clear = self.addButton('c')
        b_equal = self.addButton('=')

        # Arrange the buttons into lists which represent calculator rows
        row1 = [b7, b8, b9, b_add]
        row2 = [b4, b5, b6, b_sub]
        row3 = [b1, b2, b3, b_mult]
        row4 = [b_clear, b0, b_equal, b_div]

        # Assign each button to a particular location on the GUI
        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for buttn in row:
                buttn.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def addButton(self, value):
        return tk.Button(self.master, text=value, width=16, height=2, command=lambda: self.clickButton(str(value)))

    def clickButton(self, value):
        current_equation = str(self.equation.get())

        if value == 'c':
            self.equation.delete(-1, tk.END)

        elif value == '=':
            if current_equation[-1] in ["+", "-", "*", "/"]:
                tkm.showinfo("Warning!", "Invalid syntax. Equation does not end in a number.")
            else:
                answer = str(eval(current_equation))
                self.equation.delete(-1, tk.END)
                self.equation.insert(0, answer)

        else:
            self.equation.delete(0, tk.END)
            self.equation.insert(0, current_equation + value)


if __name__ == '__main__':
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')

    my_gui = Calculator(root)

    root.mainloop()

# (!1)
