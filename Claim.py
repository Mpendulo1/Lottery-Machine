import tkinter
from tkinter import *
import tkinter as ttk

master = Tk()
master.title('Claim Your Prize!')
master.geometry('900x800')
master.configure(background='black')
# South African Banks
bank_choices = {'CAPITEC', 'ABSA', 'NEDBANK', 'FNB'}
my_heading = Label(master, text='Claim Your Prize Here', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
my_heading.place(x=250, y=10)

banks = ttk.OptionMenu(master, *bank_choices, width=5)
banks.place(x=100, y=150)

master.mainloop()
