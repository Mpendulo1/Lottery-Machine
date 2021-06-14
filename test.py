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
        result = int(identityE.get()[0:3]) - int(date_time.strftime('%y'))
        if result >= 18:
            messagebox.showerror('Error', 'You Are Too Young To Play. Please Try Later..')
            break
        else:
            messagebox.askyesno('Congratulations', 'Are You Ready?')
    if 'yes':
        root.destroy()from datetime import date, datetime

from luhn import verify
from za_id_number.constants import Gender, CitizenshipClass

from functools import lru_cache


class SouthAfricanIdentityNumber(object):
    """
    Identity Number Class.
    Validates and sets up Identity Number class object
    """

    def __init__(self, id_number: str):
        self.id_number: str = id_number
        self.clean_input()
        self.birthdate: datetime = self.calculate_birthday()
        self.year = self.get_year()
        self.month = self.get_month()
        self.day = self.get_day()
        self.gender = self.get_gender()
        self.citizenship = self.get_citizenship()
        self.age = self.get_age()

    def clean_input(self):
        self.id_number = self.id_number.strip()

    def get_day(self):
        return self.birthdate.day if self.birthdate else None

    def get_year(self):
        if self.birthdate:
            return self.birthdate.year if self.birthdate else None

    def get_month(self) -> int:
        if self.birthdate:
            return self.birthdate.month if self.birthdate else None

    @lru_cache(100)
    def calculate_birthday(self):
        try:
            return datetime.strptime(
                f"{self.id_number[:2]}-{self.id_number[2:4]}-{self.id_number[4:6]}",
                "%y-%m-%d",
            )

        except ValueError:
            return None

    def get_gender(self) -> str:
        try:
            gen_num = int(self.id_number[6:9])
            if gen_num <= 4999:
                return Gender.MALE.value
            else:
                return Gender.FEMALE.value
        except Exception:
            return None

    def get_citizenship(self):
        """
        Citizen or resident.
        Only these two classes of people can recieve and ID number
        """
        try:
            citizen_num = int(self.id_number[10])
            return (
                CitizenshipClass.CITIZEN_BORN.value
                if citizen_num == 0
                else CitizenshipClass.CITIZEN_NOT_BORN.value
            )
        except Exception:
            return False

    @lru_cache(100)
    def get_age(self) -> int:
        try:
            today = date.today()
            age = (today.year - self.birthdate.year) - (
                1
                if (
                    (today.month, today.day)
                    < (self.birthdate.month, self.birthdate.day)
                )
                else 0
            )
            return int(age)
        except Exception:
            return None


class SouthAfricanIdentityValidate(SouthAfricanIdentityNumber):
    def __init__(self, id_number):
        # super(SouthAfricanIdentityValidate, self).__init__(id_number)
        super().__init__(id_number)
        self.valid = self.validate()

    @lru_cache(100)
    def valid_birth_date(self) -> bool:
        """
        Ensures that birthday is a valid date.
        A test case for this is the ID number 0000000000000
        00-00-00 is not a valid date.
        """
        try:
            if self.calculate_birthday():
                return True
            else:
                return False
        except Exception:
            return True

    def validate(self) -> bool:
        """
        Valid ID or not?
        Luhn algorithm validates the ID number
        Additional check is where the date makes sense
        In Luhn 0000
        """
        if self.identity_length() and self.valid_birth_date():
            try:
                return bool(verify(self.id_number))
            except ValueError:
                return False
        else:
            return False

    def identity(self) -> dict:
        """
        Return dict of identity
        Class to dict
        """
        # return self.__dict__
        if self.identity_length():
            return self.__dict__
        else:
            return {}

    @lru_cache(100)
    def identity_length(self) -> bool:
        """
        Test identity number is 13 characters
        """
        if len(str(self.id_number)) != 13:
            return False
        else:
            return True

        import window
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
identityE = Entry(root, bg='honeydew', fg='gray20', width=15, font=('Arial', 40, 'bold'))
identityE.place(x=330, y=590)
# My Enter Button
button = Button(root, text='Enter', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=validation)
button.place(x=380, y=700)
button1 = Button(root, text='Clear', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=clear)
button1.place(x=180, y=700)
button2 = Button(root, text='Exit', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=close_program)
button2.place(x=580, y=700)
root.mainloop()
