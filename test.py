
def play_lotto():
    my_lotto_numbers = number_entry.get()
    my_lotto_numbers2 = number_entry2.get()
    my_lotto_numbers3 = number_entry3.get()
    my_lotto_list = [my_lotto_numbers]
    my_lotto_list2 = [my_lotto_numbers2]
    my_lotto_list3 = [my_lotto_numbers3]
    my_lotto_list.sort()bh
    my_lotto_list2.sort()
    my_lotto_list3.sort()

    lotto_num = sorted(random.sample(range(1, 49), 6))
    if any(my_lotto_list) < 0 or any(my_lotto_list) and any(my_lotto_list2) < 0 or any(my_lotto_list2) and any(my_lotto_list3) < 0 or any(my_lotto_list3) < 50:
        messagebox.showinfo('Lets Play', 'Get Ready')

        if len(lotto_num) == len(my_lotto_list):
            equal = set(lotto_num).intersection(set(my_lotto_list))
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
            messagebox.showerror('SORRY', "Please TRY AGAIN" + str(lotto_num))
            lotto_entry.config(str(lotto_num))
            return

# ----------------------------------------------
def adding(add):
if len(entry1) < 6 and add not in entry1:
entry1.append(add)
self.ent1.config(entry1)

elif len(entry1) == 6 and len(entry2) < 6 and add not in entry2:
entry2.append(add)
ent2.config(text=entry2)
elif len(entry2) == 6 and len(entry3) < 6 and add not in entry3:
entry3.append(add)
self.ent3.config(text=entry3)

else:
if len(entry3) == 6:
messagebox.showerror("Error","Tries are full")
else:
messagebox.showerror("Error","you can only select the same number once per entry")
# -----------------------------------------------------------------------------------------------
def play(self):

if len(empty1) <= 6:
for i in self.game_numbers:
if i in empty1:
compare.append(i)

num_entry1.insert(0, empty1)
lotto_numbers.insert(0, compare)
draw_entry1.insert(0, game_numbers)

elif len(self.empty2) <= 6:


for i in self.game_numbers:
if i in self.empty2:
self.compare.append(i)

self.num_entry2.insert(0,self.empty2)
self.results_entry2.insert(0,self.compare)
self.draw_entry2.insert(0,self.game_numbers)

else:
if len(self.empty3) <= 6:
for i in self.game_numbers:
if i in self.empty3:
self.compare.append(i)

self.num_entry3.insert(0,self.empty3)
self.results_entry3.insert(0,self.compare)
self.draw_entry3.insert(0,self.game_nu
