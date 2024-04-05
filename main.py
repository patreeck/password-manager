from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import random
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genpass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_let = [random.choice(letters) for _ in range(randint(8, 10))]
    password_sym = [random.choice(symbols) for _ in range(randint(2, 4))]
    password_num = [random.choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_let + password_sym + password_num

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website=web_entry.get()
    email=email_entry.get()
    passw= pass_entry.get()
    new_data={
        website :{
            "email" :email,
            "password" : passw
        }
    }
    if len(website) != 0 and len(passw) !=0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered, EMAIL : {email} \n "
                                                      f"PASSWORD: {passw}\n is it ok to save ? ")
        if is_ok:
            try:
                with open("data.json", mode='r') as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("data.json", mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode='w') as file:
                    json.dump(data,file, indent=4)
            finally:
                web_entry.delete(0,END)
                pass_entry.delete(0,END)
    else:
        messagebox.showwarning(message="Please fill all the information")

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_pass():
    website = web_entry.get()
    if len(website) != 0:
        try:
            with open("data.json", mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title=website, message=f"No data found for {website} entry !")
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f"USERNAME: {data[website]["email"]}\n "
                                                       f"Password: {data[website]["password"]}")
            else:
                messagebox.showwarning(title=website, message=f"No data found for {website} entry !")

    else:
        messagebox.showwarning(message="Please Enter website name")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

web_label=Label(text="Website")
web_label.grid(row=1, column=0)
web_entry= Entry( width= 21)
web_entry.focus_set()
web_entry.grid(row=1, column=1)

search_button= Button(text="Search", width=20, command=find_pass)
search_button.grid(row=1, column=2)

email_label=Label(text="Email/Username")
email_label.grid(row=2, column=0)
email_entry= Entry( width= 35)
email_entry.insert(0,"pratik.gadkar@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pass_label=Label(text="Password")
pass_label.grid(row=3, column=0)
pass_entry= Entry( width= 21)
pass_entry.grid(row=3, column=1)

gen_button= Button(text="Generate Password", width=20, command=genpass)
gen_button.grid(row=3, column=2)

gen_button= Button(text="Add", width=30, command=save_pass)
gen_button.grid(row=4, column=1, columnspan=2)

window.mainloop()