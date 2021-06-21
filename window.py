import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
from playsound import playsound


root = Tk()
root.title('Lottery Machine')
root.geometry('900x1100')
root.configure(background='black')
# My Functions

image = Image.open('lotto.jpg')
test = ImageTk.PhotoImage(image)
label1 = tkinter.Label(image=test)
label1.image = test
# Position of my Image
label1.place(x=-300, y=0)

# function
texts = StringVar
empty_list = []
empty_list2 = []
empty_list3 = []

def lotto_plus():
    y = 0
    lotto_random_numbers = sorted(random.sample(range(0, 49), 6))
    for x in range(0, 6):
        if empty_list[x] == lotto_random_numbers[x]:
            y += 1
    if y == 6:
        playsound('jackpot.mp3')
        messagebox.Message('JACKPOT', 'Congratulations, You Have Won R1,000,000.00')
        root.destroy()
        import Claim
    elif y == 5:
        messagebox.Message('Congrats', 'You Have Won R8,584.00')
        root.destroy()
        import Claim
    elif y == 4:
        messagebox.showinfo('Hurray', 'You Have Won R2,384.00')
        root.destroy()
        import Claim
    elif y == 3:
        messagebox.showinfo('Hurray', 'You Have Won R100.50')
        root.destroy()
        import Claim
    elif y == 2:
        messagebox.showinfo('Nice Try', 'You Got Two Numbers Correct: R20.00')
        root.destroy()
        import Claim
    elif y < 1:
        messagebox.showinfo('Hard Luck', 'Only One Number That Matches: Lotto Plus ' + str(lotto_random_numbers) + '\nYour Numbers: ' + str(empty_list))

    else:
        playsound('Oh no.mp3')
        messagebox.askretrycancel('Tough Luck!', "NO MATCHING NUMBERS FOUND")


        return

def power_ball():
    y = 0
    lotto_random_numbers = sorted(random.sample(range(0, 49), 6))
    for i in range(0, 6):
        if empty_list2[i] == lotto_random_numbers[i]:
            y += 1
    if y == 6:
        playsound('jackpot.mp3')
        messagebox.Message('JACKPOT!!!!', 'Congratulations, You have won R1,000,000.00')
        root.destroy()
        import Claim

    elif y == 5:
        messagebox.Message('CONGRATS', 'You have won R8,584.00')
        root.destroy()
        import Claim
    elif y == 4:
        messagebox.showinfo('Hurray''You have won R2,384.00')
        root.destroy()
        import Claim
    elif y == 3:
        messagebox.showinfo('Hurray', 'You have won R100.50')
        root.destroy()
        import Claim
    elif y == 2:
        messagebox.showinfo('Nice Try', 'You got Two numbers correct: R20.00')
        root.destroy()
        import Claim
    elif y < 1:
         playsound('Oh no.pm3')
         messagebox.showinfo('Hard Luck', 'No Numbers That Match: Power Ball ' + str(lotto_random_numbers) + '\nYour Numbers: ' + str(empty_list2))

    else:
        playsound('Oh no.mp3')
        messagebox.askretrycancel('Tough Luck!', "NO MATCHING NUMBERS FOUND")
        return


def lotto():
    lotto_plus()
    power_ball()
    y = 0
    lotto_random_numbers = sorted(random.sample(range(0, 49), 6))
    for j in range(0, 6):
        if empty_list3[j] == lotto_random_numbers[j]:
            y += 1
    if y == 6:
        playsound('jackpot.mp3')
        messagebox.Message('JACKPOT', 'Congratulations, You Have Won R1,000,000.00')
    elif y == 5:
        messagebox.Message('Congrats', 'You Have Won R8,584.00')
        root.destroy()
        import Claim
    elif y == 4:
        messagebox.showinfo('Hurray', 'You Have Won R2,384.00')
        root.destroy()
        import Claim
    elif y == 3:
        messagebox.showinfo('Hurray', 'You Have Won R100.50')
        root.destroy()
        import Claim
    elif y == 2:
        messagebox.showinfo('Nice Try', 'You Got Two Numbers Correct: R20.00')
        root.destroy()
        import  Claim
    elif y < 1:
        messagebox.showinfo('Hard Luck', 'No Numbers That Match: Lotto ' + str(lotto_random_numbers) + '\nYour Numbers: ' + str(empty_list3))
    else:
        playsound('Oh no.mp3')
        messagebox.askretrycancel('Tough Luck!', "NO MATCHING NUMBERS FOUND")
        return


def number_selector(number):
    if len(empty_list) <= 5 and number not in empty_list:
        empty_list.append(number)
        number_entry.config(text=empty_list)

    elif len(empty_list) == 6 and len(empty_list2) <= 5 and number not in empty_list2:
        empty_list2.append(number)
        number_entry2.config(text=empty_list2)

    elif len(empty_list2) == 6 and len(empty_list3) <= 5 and number not in empty_list3:
        empty_list3.append(number)
        number_entry3.config(text=empty_list3)

    else:
        messagebox.showerror('Error', 'You Cannot Enter The Same Number!')

# active entries
# Lotto Plus
def lotto_entry_1():
    number_entry.configure(state='normal')
    number_entry2.configure(state='disable')
    number_entry3.configure(state='disable')

# Power Ball
def lotto_entry_2():
    number_entry.configure(state='disable')
    number_entry2.configure(state='normal')
    number_entry3.configure(state='disable')

# Lotto
def lotto_entry_3():
    number_entry.configure(state='disable')
    number_entry2.configure(state='disable')
    number_entry3.configure(state='normal')

# Clear Button
def clear():
    number_entry.config(text="")
    number_entry2.config(text="")
    number_entry3.config(text="")
# Exit Button
def close():
    root.destroy()


# my heading
my_heading = Label(root, text='Come On Let"s Play!:', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
my_heading.place(x=0, y=10)

top_frame = Frame(root, bg="cyan", width=480, height=500)
top_frame.place(x=200, y=50)

button1 = Button(top_frame, text='1', width=1, bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('1 '))
button1.place(x=0, y=0)

button2 = Button(top_frame, text='2', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('2 '))
button2.place(x=70, y=0)

button3 = Button(top_frame, text='3', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('3 '))
button3.place(x=140, y=0)

button4 = Button(top_frame, text='4', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('4 '))
button4.place(x=210, y=0)

button5 = Button(top_frame, text='5', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('5 '))
button5.place(x=280, y=0)

button6 = Button(top_frame, text='6', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('6 '))
button6.place(x=350, y=0)

button7 = Button(top_frame, text='7', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('7 '))
button7.place(x=420, y=0)

button8 = Button(top_frame, text='8', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('8 '))
button8.place(x=0, y=70)

button9 = Button(top_frame, text='9', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: number_selector('9 '))
button9.place(x=70, y=70)

button10 = Button(top_frame, text='10', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('10 '))
button10.place(x=140, y=70)

button11 = Button(top_frame, text='11', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('11 '))
button11.place(x=210, y=70)

button12 = Button(top_frame, text='12', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('12 '))
button12.place(x=280, y=70)

button13 = Button(top_frame, text='13', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('13 '))
button13.place(x=350, y=70)

button14 = Button(top_frame, text='14', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('14 '))
button14.place(x=420, y=70)


button15 = Button(top_frame, text='15', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('15 '))
button15.place(x=0, y=140)

button16 = Button(top_frame, text='16', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('16 '))
button16.place(x=70, y=140)

button17 = Button(top_frame, text='17', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('17 '))
button17.place(x=140, y=140)

button18 = Button(top_frame, text='18', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('18 '))
button18.place(x=210, y=140)

button19 = Button(top_frame, text='19', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('19 '))
button19.place(x=280, y=140)

button20 = Button(top_frame, text='20', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('20 '))
button20.place(x=350, y=140)

button21 = Button(top_frame, text='21', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('21 '))
button21.place(x=420, y=140)


button22 = Button(top_frame, text='22', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('22 '))
button22.place(x=0, y=210)

button23 = Button(top_frame, text='23', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('23 '))
button23.place(x=70, y=210)

button24 = Button(top_frame, text='24', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('24 '))
button24.place(x=140, y=210)

button25 = Button(top_frame, text='25', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('25 '))
button25.place(x=210, y=210)

button26 = Button(top_frame, text='26', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('26 '))
button26.place(x=280, y=210)

button27 = Button(top_frame, text='27', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('27 '))
button27.place(x=350, y=210)

button28 = Button(top_frame, text='28', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('28 '))
button28.place(x=420, y=210)


button29 = Button(top_frame, text='29', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('29 '))
button29.place(x=0, y=280)

button30 = Button(top_frame, text='30', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('30 '))
button30.place(x=70, y=280)

button31 = Button(top_frame, text='31', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('31 '))
button31.place(x=140, y=280)

button32 = Button(top_frame, text='32', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('32 '))
button32.place(x=210, y=280)

button33 = Button(top_frame, text='33', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('33 '))
button33.place(x=280, y=280)

button34 = Button(top_frame, text='34', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('34 '))
button34.place(x=350, y=280)

button35 = Button(top_frame, text='35', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('35 '))
button35.place(x=420, y=280)


button36 = Button(top_frame, text='36', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('36 '))
button36.place(x=0, y=350)

button37 = Button(top_frame, text='37', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('37 '))
button37.place(x=70, y=350)

button38 = Button(top_frame, text='38', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('38 '))
button38.place(x=140, y=350)

button39 = Button(top_frame, text='39', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('39 '))
button39.place(x=210, y=350)

button40 = Button(top_frame, text='40', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('40 '))
button40.place(x=280, y=350)

button41 = Button(top_frame, text='41', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('41 '))
button41.place(x=350, y=350)

button42 = Button(top_frame, text='42', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('42 '))
button42.place(x=420, y=350)


button43 = Button(top_frame, text='43', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('43 '))
button43.place(x=0, y=420)

button44 = Button(top_frame, text='44', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('44 '))
button44.place(x=70, y=420)

button45 = Button(top_frame, text='45', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('45 '))
button45.place(x=140, y=420)

button46 = Button(top_frame, text='46', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('46 '))
button46.place(x=210, y=420)

button47 = Button(top_frame, text='47', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('47 '))
button47.place(x=280, y=420)

button48 = Button(top_frame, text='48', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('48 '))
button48.place(x=350, y=420)

button49 = Button(top_frame, text='49', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: number_selector('49 '))
button49.place(x=420, y=420)

# Number entries

number_label = Label(root, text='Lotto Plus:', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
number_label.place(x=0, y=560)
number_entry = Label(root,  bg='honeydew', fg='gray20', width=20, font=('Arial', 25, 'bold'), state="disabled")
number_entry.place(x=300, y=560)

number_label2 = Label(root, text='Power Ball:', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
number_label2.place(x=0, y=640)
number_entry2 = Label(root,  bg='honeydew', fg='gray20', width=20, font=('Arial', 25, 'bold'), state="disabled")
number_entry2.place(x=300, y=640)

number_label3 = Label(root, text='Lotto:', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
number_label3.place(x=0, y=740)
number_entry3 = Label(root,  bg='honeydew', fg='gray20', width=20, font=('Arial', 25, 'bold'), state="disabled")
number_entry3.place(x=300, y=740)

# lotto Generated Numbers
# lotto_numbers = Label(root, text='Lotto Numbers: ', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
# lotto_numbers.place(x=0, y=840)
# lotto_entry = Label(root,  bg='honeydew', fg='gray20', width=15, font=('Arial', 30, 'bold'))
# lotto_entry.place(x=300, y=840)

# MY Buttons
button = Button(root, text='Clear', bg='gray80', fg='gray12', font=('Georgia', 30, 'bold'), cursor='hand2', command=clear)
button.place(x=380, y=900)
button1 = Button(root, text='Exit', bg='gray80', fg='gray12', font=('Georgia', 30, 'bold'), cursor='hand2', command=close)
button1.place(x=180, y=900)
button2 = Button(root, text='PLAY', bg='gray80', fg='gray12', font=('Georgia', 30, 'bold'), cursor='hand2', command=lotto)
button2.place(x=580, y=900)

# My Active buttons
# Lotto Plus Active Button
# active_button1 = Button(root, text='ACTIVE', bg='gray80', fg='gray12', font=('Georgia', 10, 'bold'), cursor='hand2', command=lotto_entry_1)
# active_button1.place(x=650, y=560)
# Power Ball Active Button
# active_button2 = Button(root, text='ACTIVE', bg='gray80', fg='gray12', font=('Georgia', 10, 'bold'), cursor='hand2', command=lotto_entry_2)
# active_button2.place(x=650, y=640)
# Lotto Active Button
# active_button3 = Button(root, text='ACTIVE', bg='gray80', fg='gray12', font=('Georgia', 10, 'bold'), cursor='hand2', command=lotto_entry_3)
# active_button3.place(x=650, y=740)

root.mainloop()
