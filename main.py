# Mpendulo Khoza
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

    if "@" in email_entry.get():
        messagebox.showinfo("Email Address", "Correct Email")

    else:
        messagebox.showinfo(title='Alert!', message="Please enter valid email address!")
        email_entry.delete(0, END)

    try:

        TEXT_file = open('TEXT_file.txt', 'r+')
        TEXT_file.writelines('FullName: ' + str(fullnameE.get()) + '\n')
        TEXT_file.writelines('Email: ' + str(email_entry.get()) + '\n')
        TEXT_file.writelines('Address: ' + str(addressE.get()) + '\n')
        TEXT_file.writelines('Identity:' + str(identityE.get()) + '\n')
        TEXT_file.close()

        for x in range(int(identityE.get())):
            date_time = datetime.datetime.now()
            res = int(date_time.strftime("%y")) - int(identityE.get()[0:2])
            if res >= 18:
                messagebox.showinfo("Status", "You are qualified to play Lotto")
                root.destroy()
                import window
            elif len(identityE.get()) != 13:
                messagebox.showerror("Error", "Not a valid ID number")
                break
            else:
                messagebox.showerror("Error", "You are too young to play Lotto")
                break
    except ValueError:
        if identityE.get() != int:
            messagebox.showerror("Error", "The id number must be an integer")
        elif fullnameE.get() != str:
            messagebox.showerror("Error", "Name must be a string or in letters")


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
