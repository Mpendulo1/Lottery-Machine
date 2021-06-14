import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime

root = Tk()
root.title('Lottery Machine')
root.geometry('900x800')
root.configure(background='yellow')
# defining my function here
def validation():
    date_time = datetime.datetime.now()
    for x in range(int(identityE.get())):
        result = int(date_time.strftime('%y')) - int(identityE.get()[0:2])
        if result >= 18:
            m = messagebox.askquestion('Congratulations', 'Are You Ready?')
            if m == 'yes':
                root.destroy()
                import window
            elif m == 'no':
                pass
        else:
            messagebox.showerror('Error', 'You Are Too Young To Play. Please Try Later..')
            break

# defining my exit button
def clear():
    fullnameE.delete(0, END)
    email_entry.delete(0, END)
    addressE.delete(0, END)
    identityE.delete(0, END)
# defining my Exit Button
def close_program():
    root.destroy()

# my background image here


image = Image.open('lotto-IMAGE.jpg')
test = ImageTk.PhotoImage(image)
label1 = tkinter.Label(image=test)
label1.image = test
# Position of my Image
label1.place(x=300, y=50)

# My Details Entry form
# Name and Surname Entry
fullname = Label(root, text='Full Name:', bg='SkyBlue', fg='honeydew', font=('Arial', 40, 'bold'))
fullname.place(x=10, y=370)
fullnameE = Entry(root, bg='honeydew', fg='gray20', width=15, font=('Arial', 40, 'bold'))
fullnameE.place(x=330, y=365)
# Email Entry
label_email = Label(root, text='Email:', bg='SkyBlue', fg='honeydew', font=('Arial', 40, 'bold'))
label_email.place(x=10, y=440)
email_entry = Entry(root, bg='honeydew', fg='gray20', width=15, font=('Arial', 40, 'bold'))
email_entry.place(x=330, y=440)
# Home Address Entry
address = Label(root, text='Address:', bg='SkyBlue', fg='honeydew', font=('Arial', 40, 'bold'))
address.place(x=10, y=515)
addressE = Entry(root, bg='honeydew', fg='gray20', width=15, font=('Arial', 40, 'bold'))
addressE.place(x=330, y=515)
# Identity Entry
identity = Label(root, text='Identity:', bg='SkyBlue', fg='honeydew', font=('Arial', 40, 'bold'))
identity.place(x=10, y=590)
identityE = Entry(root, bg='honeydew', show="*", fg='gray20', width=15, font=('Arial', 40, 'bold'))
identityE.place(x=330, y=590)
# My Enter Button
button = Button(root, text='Enter', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=validation)
button.place(x=380, y=700)
button1 = Button(root, text='Clear', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=clear)
button1.place(x=180, y=700)
button2 = Button(root, text='Exit', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=close_program)
button2.place(x=580, y=700)
root.mainloop()
