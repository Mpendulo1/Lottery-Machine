import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter as ttk
from tkinter.ttk import Combobox
from playsound import playsound
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

master = Tk()
master.title('Claim Your Prize!')
master.geometry('700x600')
master.configure(background='black')

def bank_account():
    try:
        bank_fig = banks_entry.get()
        branch = label2_entry.get()
        if len(bank_fig) == 11 and len(branch) == 6:
            details_file = open("TEXT_file.txt", "a+")
            details_file.write("* Account Name: " + label1_entry.get() + " " + "| Player Account Number: " + banks_entry.get() + " " + "| Bank Branch Code: " + label2_entry.get() + "| Player Bank Type: " + banks.get() + "\n")
            details_file.close()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            sender_email_id = 'mpendulokhozamk2@gmail.com'
            TEXT_file = open('TEXT_file.txt', '+r')
            line = TEXT_file.readlines()
            reciever_email_id = 'example@gmail.com'
            password = 'Avuyonke19'
            subject = "ITHUBA National Lottery Prize Claim"
            msg = MIMEMultipart()
            msg['from'] = sender_email_id
            msg['To'] = reciever_email_id
            msg['Subject'] = subject
            body = "Congratulations!\n"
            body = body + "You have won! a prize from iTHUBA National Lottery of South Africa"

            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            s.starttls()
            s.login(sender_email_id, password)

            s.sendmail(sender_email_id, reciever_email_id, text)
            s.quit()
            messagebox.showinfo("Successful", "Please Check Your Email For Further Instructions")

        else:
            messagebox.showinfo("Failed", "You are Kindly Advised to Please Enter A 11 Digit Bank Account Number and A 6 Digit Branch Code")
    except ValueError(str):
        messagebox.showinfo("Invalid", "You are kindly Advised to Please Utilize Digits Only")


# defining my Exit Button
def close_program():
    master.destroy()

def claim_my_prize():
    pass

def play_again():
    master.destroy()
    import window


# South African Banks
bank_choices = {'CAPITEC', 'ABSA', 'NEDBANK', 'FNB'}
bankset = StringVar(master)
bankset.set("select bank")
my_heading = Label(master, text='Claim Your Prize Here', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
my_heading.place(x=150, y=10)

banks = ttk.OptionMenu(master, bankset, *bank_choices)
banks.place(x=100, y=150)

banks_entry = Entry(master, bg='honeydew', show="*", fg='gray20', width=20, font=('Arial', 20, 'bold'))
banks_entry.place(x=250, y=150)

label_1 = Label(master, text='Acc Name', bg='SkyBlue', fg='honeydew', font=('Arial', 20, 'bold'))
label_1.place(x=100, y=200)
label1_entry = Entry(master, bg='honeydew', fg='gray20', width=20, font=('Arial', 20, 'bold'))
label1_entry.place(x=250, y=200)

label_2 = Label(master, text='Branch ', bg='SkyBlue', fg='honeydew', font=('Arial', 20, 'bold'))
label_2.place(x=100, y=250)
label2_entry = Entry(master, bg='honeydew', fg='gray20', width=20, font=('Arial', 20, 'bold'))
label2_entry.place(x=250, y=250)


play_again = Button(master, text='Play Again', bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2', command=play_again)
play_again.place(x=10, y=550)

claim_prize = Button(master, text='Claim Prize', bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2', command=bank_account)
claim_prize.place(x=220, y=550)
close_win = Button(master, text='Exit', bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2', command=close_program)
close_win.place(x=440, y=550)

#currency Converter

converter_title = Label(master, text='Currency Converter', bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2')
converter_title.place(x=150, y=300)


master.mainloop()
