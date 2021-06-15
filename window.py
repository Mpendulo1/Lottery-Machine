import random
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


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
def play_lotto():
    my_lotto_numbers = lotto_entry.get()

    mylotto_list = [my_lotto_numbers]
    mylotto_list.sort()

    lotto_num = sorted(random.sample(range(1, 49), 6))
    if any(mylotto_list) < 0 or any(mylotto_list) < 50:
        messagebox.showinfo('Let"s Play', 'Get Ready')

        if len(lotto_num) == len(mylotto_list):
            equal = set(lotto_num).intersection(set(mylotto_list))
            if len(equal) == 6:
                lotto_entry.config(text='JACKPOT!!!' + "YOU JUST GOT YOURSELF PRICE; R10,000,000.00" + 'today"s lotto numbers are: ' + str(lotto_num))
            elif len(equal) == 5:
                lotto_entry.config(text='CONGRATS' + 'You got 5 Numbers Correct: R8,584.00' + str(lotto_num))
            elif len(equal) == 4:
                lotto_entry.config(text='Congrats' + 'You got 4 numbers Correct: R2,384.00' + str(lotto_num))
            elif len(equal) == 3:
                lotto_entry.config(text='Nice Try' + 'You Got 3 Numbers Correct: R100.50' + str(lotto_num))
            elif len(equal) == 2:
                lotto_entry.config(text='Nice Try' + 'You Got 2 Numbers Correct: R20.00' + str(lotto_num))
            elif len(equal) == 1:
                lotto_entry.config(text='Try Again' + 'You Got Only One Number Correct: R0.00' + str(lotto_num))
            elif len(equal) == 0:
                lotto_entry.config(text='HARD LUCK...!' + 'Non Of Your Numbers Match :(' + str(lotto_num))
        else:
            lotto_entry.config('Error', "Please TRY AGAIN")
            return


# Insert Function
def insert(val):
    number_entry.insert(END, val)
    number_entry2.insert(END, val)
    number_entry3.insert(END, val)

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


# my heading
my_heading = Label(root, text='Come On Let"s Play!:', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
my_heading.place(x=0, y=10)

top_frame = Frame(root, bg="cyan", width=480, height=500)
top_frame.place(x=200, y=50)

button1 = Button(top_frame, text='1', width=1, bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('1 '))
button1.place(x=0, y=0)

button2 = Button(top_frame, text='2', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('2 '))
button2.place(x=70, y=0)

button3 = Button(top_frame, text='3', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('3 '))
button3.place(x=140, y=0)

button4 = Button(top_frame, text='4', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('4 '))
button4.place(x=210, y=0)

button5 = Button(top_frame, text='5', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('5 '))
button5.place(x=280, y=0)

button6 = Button(top_frame, text='6', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('6 '))
button6.place(x=350, y=0)

button7 = Button(top_frame, text='7', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('7 '))
button7.place(x=420, y=0)

button8 = Button(top_frame, text='8', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('8 '))
button8.place(x=0, y=70)

button9 = Button(top_frame, text='9', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', command=lambda: insert('9 '))
button9.place(x=70, y=70)

button10 = Button(top_frame, text='10', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('10 '))
button10.place(x=140, y=70)

button11 = Button(top_frame, text='11', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('11 '))
button11.place(x=210, y=70)

button12 = Button(top_frame, text='12', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('12 '))
button12.place(x=280, y=70)

button13 = Button(top_frame, text='13', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('13 '))
button13.place(x=350, y=70)

button14 = Button(top_frame, text='14', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('14 '))
button14.place(x=420, y=70)


button15 = Button(top_frame, text='15', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('15 '))
button15.place(x=0, y=140)

button16 = Button(top_frame, text='16', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('16 '))
button16.place(x=70, y=140)

button17 = Button(top_frame, text='17', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('17 '))
button17.place(x=140, y=140)

button18 = Button(top_frame, text='18', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('18 '))
button18.place(x=210, y=140)

button19 = Button(top_frame, text='19', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('19 '))
button19.place(x=280, y=140)

button20 = Button(top_frame, text='20', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('20 '))
button20.place(x=350, y=140)

button21 = Button(top_frame, text='21', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('21 '))
button21.place(x=420, y=140)


button22 = Button(top_frame, text='22', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('22 '))
button22.place(x=0, y=210)

button23 = Button(top_frame, text='23', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('23 '))
button23.place(x=70, y=210)

button24 = Button(top_frame, text='24', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('24 '))
button24.place(x=140, y=210)

button25 = Button(top_frame, text='25', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('25 '))
button25.place(x=210, y=210)

button26 = Button(top_frame, text='26', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('26 '))
button26.place(x=280, y=210)

button27 = Button(top_frame, text='27', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('27 '))
button27.place(x=350, y=210)

button28 = Button(top_frame, text='28', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('28 '))
button28.place(x=420, y=210)


button29 = Button(top_frame, text='29', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('29 '))
button29.place(x=0, y=280)

button30 = Button(top_frame, text='30', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('30 '))
button30.place(x=70, y=280)

button31 = Button(top_frame, text='31', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('31 '))
button31.place(x=140, y=280)

button32 = Button(top_frame, text='32', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('32 '))
button32.place(x=210, y=280)

button33 = Button(top_frame, text='33', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('33 '))
button33.place(x=280, y=280)

button34 = Button(top_frame, text='34', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('34 '))
button34.place(x=350, y=280)

button35 = Button(top_frame, text='35', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('35 '))
button35.place(x=420, y=280)


button36 = Button(top_frame, text='36', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('36 '))
button36.place(x=0, y=350)

button37 = Button(top_frame, text='37', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('37 '))
button37.place(x=70, y=350)

button38 = Button(top_frame, text='38', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('38 '))
button38.place(x=140, y=350)

button39 = Button(top_frame, text='39', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('39 '))
button39.place(x=210, y=350)

button40 = Button(top_frame, text='40', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('40 '))
button40.place(x=280, y=350)

button41 = Button(top_frame, text='41', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('41 '))
button41.place(x=350, y=350)

button42 = Button(top_frame, text='42', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('42 '))
button42.place(x=420, y=350)


button43 = Button(top_frame, text='43', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('43 '))
button43.place(x=0, y=420)

button44 = Button(top_frame, text='44', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('44 '))
button44.place(x=70, y=420)

button45 = Button(top_frame, text='45', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('45 '))
button45.place(x=140, y=420)

button46 = Button(top_frame, text='46', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('46 '))
button46.place(x=210, y=420)

button47 = Button(top_frame, text='47', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('47 '))
button47.place(x=280, y=420)

button48 = Button(top_frame, text='48', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('48 '))
button48.place(x=350, y=420)

button49 = Button(top_frame, text='49', bg='gray80', fg='gray12', font=('Georgia', 35, 'bold'), cursor='hand2', width=1, command=lambda: insert('49 '))
button49.place(x=420, y=420)

# Number entries

number_label = Label(root, text='Lotto Plus:', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
number_label.place(x=0, y=560)
number_entry = Entry(root,  bg='honeydew', fg='gray20', width=15, font=('Arial', 30, 'bold'), state="disabled")
number_entry.place(x=300, y=560)

number_label2 = Label(root, text='Power Ball:', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
number_label2.place(x=0, y=640)
number_entry2 = Entry(root,  bg='honeydew', fg='gray20', width=15, font=('Arial', 30, 'bold'), state="disabled")
number_entry2.place(x=300, y=640)

number_label3 = Label(root, text='Lotto:', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
number_label3.place(x=0, y=740)
number_entry3 = Entry(root,  bg='honeydew', fg='gray20', width=15, font=('Arial', 30, 'bold'), state="disabled")
number_entry3.place(x=300, y=740)

# lotto Generated Numbers
lotto_numbers = Label(root, text='Lotto Numbers: ', bg='black', fg='honeydew', font=('Arial', 30, 'bold'))
lotto_numbers.place(x=0, y=840)
lotto_entry = Entry(root,  bg='honeydew', fg='gray20', width=15, font=('Arial', 30, 'bold') )
lotto_entry.place(x=300, y=840)

# MY Buttons
button = Button(root, text='Clear', bg='gray80', fg='gray12', font=('Georgia', 30, 'bold'), cursor='hand2',)
button.place(x=380, y=900)
button1 = Button(root, text='Exit', bg='gray80', fg='gray12', font=('Georgia', 30, 'bold'), cursor='hand2', )
button1.place(x=180, y=900)
button2 = Button(root, text='PLAY', bg='gray80', fg='gray12', font=('Georgia', 30, 'bold'), cursor='hand2', command=play_lotto)
button2.place(x=580, y=900)

# My Active buttons
# Lotto Plus Active Button
active_button1 = Button(root, text='ACTIVE', bg='gray80', fg='gray12', font=('Georgia', 10, 'bold'), cursor='hand2', command=lotto_entry_1)
active_button1.place(x=650, y=560)
# Power Ball Active Button
active_button2 = Button(root, text='ACTIVE', bg='gray80', fg='gray12', font=('Georgia', 10, 'bold'), cursor='hand2', command=lotto_entry_2)
active_button2.place(x=650, y=640)
# Lotto Active Button
active_button3 = Button(root, text='ACTIVE', bg='gray80', fg='gray12', font=('Georgia', 10, 'bold'), cursor='hand2', command=lotto_entry_3)
active_button3.place(x=650, y=740)

root.mainloop()
