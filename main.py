from tkinter import *
from Solver import solver


def inserter(value):
    output.delete('0.0', END)
    output.insert('0.0', value)


# ax^3 + bx^2 + cx + d = 0
def solve():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        d_val = float(d.get())
    except ValueError:
        inserter('Проверьте введенные данные')

    inserter(solver(a_val, b_val, c_val, d_val))


root = Tk()
root.title('Калькулятор кубических уравнений')
root.geometry('800x200+300+300')
f_top = Frame(root)
f_bot = Frame(root)
f_top.pack()
f_bot.pack()

a = Entry(f_top, width=5, font='Arial 15')
a.pack(side=LEFT, pady=10, padx=10)
Label(f_top, text='x^3 +', font='Arial 15').pack(side=LEFT, pady=10)

b = Entry(f_top, width=5, font='Arial 15')
b.pack(side=LEFT, pady=10, padx=10)
Label(f_top, text='x^2 +', font='Arial 15').pack(side=LEFT, pady=10)

c = Entry(f_top, width=5, font='Arial 15')
c.pack(side=LEFT, pady=10, padx=10)
Label(f_top, text='x +', font='Arial 15').pack(side=LEFT, pady=10)

d = Entry(f_top, width=5, font='Arial 15')
d.pack(side=LEFT, pady=10, padx=10)
Label(f_top, text='= 0', font='Arial 15').pack(side=LEFT, pady=10)

Button(f_top, text='Решить', font='Arial 12 bold', command=solve).pack(side=LEFT, pady=10, padx=10)

output = Text(f_bot, bg='black', fg='lime', font='Arial 12')
output.pack(expand=1, fill=BOTH, side=LEFT)

root.mainloop()
